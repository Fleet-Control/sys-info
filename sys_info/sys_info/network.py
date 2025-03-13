# socket for ip address
import socket
from collections import OrderedDict

# network devices
import psutil


def _find_single_ipv4_address(addrs):
    for addr in addrs:
        if addr.family == socket.AddressFamily.AF_INET:  # IPv4
            return addr.address


def get_ipv4_address(interface_name=None):
    if_addrs = psutil.net_if_addrs()

    if isinstance(interface_name, str) and interface_name in if_addrs:
        addrs = if_addrs.get(interface_name)
        address = _find_single_ipv4_address(addrs)
        return address if isinstance(address, str) else ""
    else:
        if_stats = psutil.net_if_stats()
        # remove loopback
        if_stats_filtered = {
            key: if_stats[key]
            for key, stat in if_stats.items()
            if "loopback" not in stat.flags
        }
        # sort interfaces by
        # 1. Up/Down
        # 2. Duplex mode (full: 2, half: 1, unknown: 0)
        if_names_sorted = [
            stat[0] for stat in sorted(
                if_stats_filtered.items(),
                key=lambda x: (x[1].isup, x[1].duplex),
                reverse=True)]
        if_addrs_sorted = OrderedDict(
            (key, if_addrs[key]) for key in if_names_sorted if key in if_addrs)

        for _, addrs in if_addrs_sorted.items():
            address = _find_single_ipv4_address(addrs)
            if isinstance(address, str):
                return address

        return ""
