from __future__ import annotations

import asyncio
import json

import pydantic

import slurm_viewer
import slurm_viewer.data
import slurm_viewer.data.config
from slurm_viewer.data.legacy_text_output_tools import create_node_info, create_queue_info, create_node
from slurm_viewer.data.models import Job, Node, Queue, Priority, SlurmError


class SlurmLocal:
    def __init__(self, _cluster: slurm_viewer.data.config.Cluster) -> None:
        self._cluster = _cluster

    def cluster(self) -> slurm_viewer.data.config.Cluster:
        return self._cluster

    @staticmethod
    async def partitions() -> list[str]:
        cmd = 'sinfo --format=%R --noheader'

        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await proc.communicate()

        return stdout.decode().splitlines()

    async def nodes(self) -> list[Node]:
        cmd = 'scontrol show nodes --json'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        if process.returncode == 0:
            node_list = []
            for node_dict in json.loads(stdout)['nodes']:
                node = create_node(node_dict, self._cluster.node_name_ignore_prefix)
                if node is None:
                    continue
                node_list.append(node)
            return node_list

        # Fallback in case cluster doesn't support json output.
        cmd = 'scontrol --oneliner show nodes'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        if process.returncode != 0:
            raise SlurmError(cluster=self._cluster, func='scontrol show nodes failed')

        nodes = []
        for node_str in stdout.splitlines():
            node_info = create_node_info(node_str.decode(), self._cluster)
            if node_info is None:
                continue

            nodes.append(node_info)

        return nodes

    async def queue(self) -> list[Queue]:
        def _partitions_argument(_partitions: list[str]) -> str:
            if len(_partitions) == 0:
                return ''

            return '--partition ' + ','.join(self._cluster.partitions)

        cmd = f'squeue {_partitions_argument(self._cluster.partitions)} --format=%all'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        if process.returncode != 0:
            raise SlurmError(cluster=self._cluster, func=f'squeue failed, {process.returncode=}: {cmd}')

        return create_queue_info(stdout.decode().splitlines())  # type: ignore

    async def jobs(self, num_weeks: int) -> list[Job]:
        if len(self._cluster.partitions) == 0:
            raise SlurmError(cluster=self._cluster, func='sacct failed, no partitions specified')

        partitions = ",".join(self._cluster.partitions)

        cmd = f'sacct --starttime now-{num_weeks}week --long --allusers --parsable2 --partition={partitions}'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        if process.returncode != 0:
            raise SlurmError(cluster=self._cluster, func=f'sacct failed, {process.returncode=}: {cmd}')

        lines = stdout.decode().splitlines()

        if len(lines) == 0:
            return []

        header = lines[0].rstrip().split('|')
        try:
            return [Job(**dict(zip(header, x.rstrip().split('|')))) for x in
                    lines[1:]]
        except pydantic.ValidationError:
            return []

    async def priority(self) -> list[Priority]:
        partitions = ",".join(self._cluster.partitions)
        cmd = f'"sprio --partition={partitions}"'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        header = list(Priority.model_fields.keys())

        lines = stdout.decode().splitlines()
        if len(lines) == 0:
            return []

        result = []
        for line in lines[1:]:  # skip the first row (it's the header)
            result.append(Priority(**dict(zip(header, line.rstrip().split('|')))))

        return result

    @staticmethod
    async def users(group: str) -> list[str]:
        cmd = f'getent group {group}'

        process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                        stderr=asyncio.subprocess.PIPE)
        stdout, _ = await process.communicate()

        return sorted(stdout.decode().rsplit(':', maxsplit=1)[-1].split(','))
