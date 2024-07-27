"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://docs.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule
versions = {
    '100.0.1185': {'minor_range': (0, 99), 'webkit': '537.36'},
    '101.0.1210': {'minor_range': (0, 99), 'webkit': '537.36'},
    '102.0.1245': {'minor_range': (0, 99), 'webkit': '537.36'},
    '103.0.1264': {'minor_range': (0, 99), 'webkit': '537.36'},
    '104.0.1293': {'minor_range': (0, 99), 'webkit': '537.36'},
    '105.0.1343': {'minor_range': (0, 99), 'webkit': '537.36'},
    '106.0.1370': {'minor_range': (0, 99), 'webkit': '537.36'},
    '107.0.1418': {'minor_range': (0, 99), 'webkit': '537.36'},
    '108.0.1462': {'minor_range': (0, 99), 'webkit': '537.36'},
    '109.0.1518': {'minor_range': (0, 99), 'webkit': '537.36'},
    '110.0.1587': {'minor_range': (0, 99), 'webkit': '537.36'},
    '111.0.1661': {'minor_range': (0, 99), 'webkit': '537.36'},
    '112.0.1722': {'minor_range': (0, 99), 'webkit': '537.36'},
    '113.0.1774': {'minor_range': (0, 99), 'webkit': '537.36'},
    '114.0.1823': {'minor_range': (0, 99), 'webkit': '537.36'},
    '115.0.1901': {'minor_range': (0, 99), 'webkit': '537.36'},
    '116.0.1938': {'minor_range': (0, 99), 'webkit': '537.36'},
    '117.0.2045': {'minor_range': (0, 99), 'webkit': '537.36'},
    '118.0.2088': {'minor_range': (0, 99), 'webkit': '537.36'},
    '119.0.2151': {'minor_range': (0, 99), 'webkit': '537.36'},
    '120.0.2210': {'minor_range': (0, 99), 'webkit': '537.36'},
    '121.0.2277': {'minor_range': (0, 99), 'webkit': '537.36'},
    '122.0.2365': {'minor_range': (0, 99), 'webkit': '537.36'},
    '123.0.2420': {'minor_range': (0, 99), 'webkit': '537.36'},
    '124.0.2478': {'minor_range': (0, 99), 'webkit': '537.36'},
    '125.0.2535': {'minor_range': (0, 99), 'webkit': '537.36'},
    '126.0.2592': {'minor_range': (0, 99), 'webkit': '537.36'},
    '127.0.2651': {'minor_range': (0, 99), 'webkit': '537.36'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
