from __future__ import annotations

import asyncio

import asyncssh
import pydantic

import slurm_viewer
import slurm_viewer.data
import slurm_viewer.data.config
from slurm_viewer.data.legacy_text_output_tools import create_node_info, create_queue_info
from slurm_viewer.data.models import Node, Queue, Job, SlurmError

TIMEOUT = 10  # seconds


class SlurmSsh:
    def __init__(self, _cluster: slurm_viewer.data.config.Cluster) -> None:
        self._cluster = _cluster
        self.connection: asyncssh.SSHClientConnection | None = None
        self._lock = asyncio.Lock()

    def __del__(self) -> None:
        if self.connection:
            print('closing connection')
            self.connection.close()

    def cluster(self) -> slurm_viewer.data.config.Cluster:
        return self._cluster

    async def _connect(self) -> None:
        async with self._lock:
            if self.connection is not None:
                return
            print('opening connection')
            self.connection = await asyncssh.connect(self._cluster.server)
            assert self.connection is not None

    async def partitions(self) -> list[str]:
        await self._connect()
        assert self.connection is not None

        cmd = 'sinfo --format=%R --noheader'
        result = await self.connection.run(cmd, check=True, timeout=TIMEOUT)
        assert isinstance(result.stdout, str)
        return result.stdout.splitlines()

    async def nodes(self) -> list[Node]:
        await self._connect()
        assert self.connection is not None

        cmd = 'scontrol --oneliner show nodes'
        result = await self.connection.run(cmd, check=True, timeout=TIMEOUT)
        assert result
        assert isinstance(result.stdout, str)

        lines = result.stdout.splitlines()

        nodes = []
        for node_str in lines:
            node_info = create_node_info(node_str, self._cluster)
            if node_info is None:
                continue

            nodes.append(node_info)
        return nodes

    async def queue(self) -> list[Queue]:
        def _partitions_argument(_partitions: list[str]) -> str:
            if len(_partitions) == 0:
                return ''

            return '--partition ' + ','.join(_partitions)

        await self._connect()
        assert self.connection is not None

        cmd = f'squeue {_partitions_argument(self._cluster.partitions)} --format=%all'

        result = await self.connection.run(cmd, check=True, timeout=TIMEOUT)
        assert result
        assert result.stdout
        assert isinstance(result.stdout, str)

        return create_queue_info(result.stdout.splitlines())  # type: ignore

    async def jobs(self, num_weeks: int = 4) -> list[Job]:
        await self._connect()
        assert self.connection is not None

        cmd = (f'sacct --starttime now-{num_weeks}week --long --allusers --parsable2 '
               f'--partition={",".join(self._cluster.partitions)}')
        try:
            result = await self.connection.run(cmd, check=True, timeout=TIMEOUT)
        except asyncssh.process.TimeoutError as e:
            raise SlurmError(cluster=self._cluster, func='jobs') from e

        assert result
        assert result.stdout
        assert isinstance(result.stdout, str)

        lines = result.stdout.splitlines()

        if len(lines) == 0:
            return []

        header = lines[0].rstrip().split('|')
        try:
            return [Job(**dict(zip(header, x.rstrip().split('|')))) for x in lines[1:]]
        except pydantic.ValidationError:
            return []
