import sys

from qbittorrent import Client


qb = Client('')
qb.login()
torrent = sys.argv[1]
qb.download_from_link(torrent)