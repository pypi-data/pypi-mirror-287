"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random

# https://chromereleases.googleblog.com/search/label/Stable%20updates
versions = {
    '100.0.4896': {'minor_range': (0, 255), 'webkit': '537.36'},
    '101.0.4951': {'minor_range': (0, 255), 'webkit': '537.36'},
    '102.0.5005': {'minor_range': (0, 255), 'webkit': '537.36'},
    '103.0.5060': {'minor_range': (0, 255), 'webkit': '537.36'},
    '104.0.5112': {'minor_range': (0, 255), 'webkit': '537.36'},
    '105.0.5195': {'minor_range': (0, 255), 'webkit': '537.36'},
    '106.0.5249': {'minor_range': (0, 255), 'webkit': '537.36'},
    '107.0.5304': {'minor_range': (0, 255), 'webkit': '537.36'},
    '108.0.5359': {'minor_range': (0, 255), 'webkit': '537.36'},
    '109.0.5414': {'minor_range': (0, 255), 'webkit': '537.36'},
    '110.0.5481': {'minor_range': (0, 255), 'webkit': '537.36'},
    '111.0.5563': {'minor_range': (0, 255), 'webkit': '537.36'},
    '112.0.5615': {'minor_range': (0, 255), 'webkit': '537.36'},
    '114.0.5735': {'minor_range': (0, 255), 'webkit': '537.36'},
    '115.0.5790': {'minor_range': (0, 255), 'webkit': '537.36'},
    '116.0.5845': {'minor_range': (0, 255), 'webkit': '537.36'},
    '117.0.5938': {'minor_range': (0, 255), 'webkit': '537.36'},
    '118.0.5993': {'minor_range': (0, 255), 'webkit': '537.36'},
    '119.0.6045': {'minor_range': (0, 255), 'webkit': '537.36'},
    '120.0.6099': {'minor_range': (0, 255), 'webkit': '537.36'},
    '121.0.6167': {'minor_range': (0, 255), 'webkit': '537.36'},
    '122.0.6261': {'minor_range': (0, 255), 'webkit': '537.36'},
    '123.0.6312': {'minor_range': (0, 255), 'webkit': '537.36'},
    '124.0.6367': {'minor_range': (0, 255), 'webkit': '537.36'},
    '125.0.6422': {'minor_range': (0, 255), 'webkit': '537.36'},
    '126.0.6478': {'minor_range': (0, 255), 'webkit': '537.36'},
    '127.0.6533': {'minor_range': (0, 255), 'webkit': '537.36'},
}


def get_version():
    choice = random.randint(0, len(versions) - 1)
    i = 0
    for major, props in versions.items():
        if choice == i:
            minor = random.randint(int(props['minor_range'][0]), int(props['minor_range'][1]))
            return {'major': major, 'minor': minor, 'webkit': props['webkit']}
        i = i + 1
