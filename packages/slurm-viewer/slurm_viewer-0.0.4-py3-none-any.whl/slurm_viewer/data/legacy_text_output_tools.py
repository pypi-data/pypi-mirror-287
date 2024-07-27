from __future__ import annotations

import re

from slurm_viewer.data.config import Cluster
from slurm_viewer.data.models import Node, Queue

NODE_RE = (r'^NodeName=(?P<node_name>.+?)\s+Arch=(?P<arch>.+?)\s+CoresPerSocket=(?P<cores_per_socket>\d+)\s+'
           r'CPUAlloc=(?P<cpu_alloc>\d+)\s+CPUEfctv=(?P<cpu_efctv>\d+)\s+CPUTot=(?P<cpu_tot>\d+)\s+'
           r'CPULoad=(?P<cpuload>\d+\.\d+)\s+AvailableFeatures=(?P<available_features>.+?)\s+'
           r'ActiveFeatures=(?P<active_features>.+?)\s+Gres=(?P<gres>.+?)\s+NodeAddr=(?P<node_addr>.+?)\s+'
           r'NodeHostName=(?P<node_hostname>.+?)\s+Version=(?P<version>.+?)\s+OS=(?P<os>.+?)\s+'
           r'RealMemory=(?P<real_memory>\d+)\s+AllocMem=(?P<alloc_mem>\d+)\s+FreeMem=(?P<freemem>\d+)\s+'
           r'Sockets=(?P<sockets>\d+)\s+Boards=(?P<boards>\d+)\s+State=(?P<state>.+?)\s+'
           r'ThreadsPerCore=(?P<threads_per_core>\d+)\s+TmpDisk=(?P<tmp_disk>\d+)\s+Weight=(?P<weight>.+?)\s+'
           r'Owner=(?P<owner>.+?)\s+MCS_label=(?P<mcs_label>.+?)\s+Partitions=(?P<partitions>.+?)\s+'
           r'BootTime=(?P<boot_time>.+?)\s+SlurmdStartTime=(?P<slurmd_start_time>.+?)\s+'
           r'LastBusyTime=(?P<last_busy_time>.+?)\s+ResumeAfterTime=(?P<resume_after_time>.+?)\s+'
           r'CfgTRES=(?P<cfgtres>.+?)\s+AllocTRES=(?P<alloc_tres>.+?)\s+')


QUEUE_RE = (r'^(?P<account>[\w\d-]+)[|](?P<tres_per_node>[\w\:]+)[|](?P<min_cpu>\d+)[|](?P<min_tmp_disk>\d+)[|]'
            r'(?P<end_time>[\w\d:-]+)[|](?P<features>[^|]+)[|](?P<group>[^|]+)[|](?P<over_subscribe>[^|]+)[|]'
            r'(?P<job_id>\d+)[|](?P<name>[^|]+)[|](?P<comment>[^|]+)[|](?P<time_limit>[^|]+)[|]'
            r'(?P<min_memory>[^|]+)[|](?P<req_nodes>[^|]*)[|](?P<command>[^|]+)[|](?P<priority>[^|]+)[|]'
            r'(?P<qos>[^|]+)[|](?P<reason>[^|]+)[|](?P<st>[^|]+)[|](?P<user>[^|]+)[|](?P<reservation>[^|]+)[|]'
            r'(?P<wc_key>[^|]+)[|](?P<excluded_nodes>[^|]*)[|](?P<nice>[^|]+)[|](?P<s_c_t>[^|]+)[|]'
            r'(?P<job_id_2>[^|]+)[|](?P<exec_host>[^|]+)[|](?P<cpus>[^|]+)[|](?P<nodes>[^|]+)[|]'
            r'(?P<dependency>[^|]+)[|](?P<array_job_id>[^|]+)[|](?P<group_2>[^|]+)[|](?P<sockets_per_node>[^|]+)[|]'
            r'(?P<cores_per_socket>[^|]+)[|](?P<threads_per_core>[^|]+)[|](?P<array_task_id>[^|]+)[|]'
            r'(?P<time_left>[^|]+)[|](?P<time>[^|]+)[|](?P<nodelist>[^|]*)[|](?P<contiguous>[^|]+)[|]'
            r'(?P<partition>[^|]+)[|](?P<priority_2>[^|]+)[|](?P<nodelist_reason>[^|]+)[|](?P<start_time>[^|]+)[|]'
            r'(?P<state>[^|]+)[|](?P<uid>[^|]+)[|](?P<submit_time>[^|]+)[|](?P<licenses>[^|]+)[|](?P<core_spec>[^|]+)[|]'
            r'(?P<scheduled_nodes>[^|]+)[|](?P<work_dir>[^|]+)$')


def create_node(_node_dict: dict, _node_name_ignore_prefix: list[str]) -> Node:
    node = Node(**_node_dict)
    for ignore_prefix in _node_name_ignore_prefix:
        if node.node_name.startswith(ignore_prefix):
            node.node_name = node.node_name.removeprefix(ignore_prefix)
            break
    return node


def create_node_info(node_str: str, cluster: Cluster) -> Node | None:
    m = re.search(NODE_RE, node_str)
    if not m:
        return None

    return create_node(m.groupdict(), cluster.node_name_ignore_prefix)


def create_queue_info(lines: list[str]) -> list[Queue]:
    def _create_queue(data: str) -> Queue | None:
        m = re.search(QUEUE_RE, data)
        if not m:
            return None

        return Queue(**m.groupdict())

    result = []
    for x in lines[1:]:
        val = _create_queue(x.rstrip())
        if val is None:
            continue

        result.append(val)

    return result
