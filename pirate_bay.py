from tpblite import TPB
from tpblite import CATEGORIES, ORDERS

t = TPB('https://pbays.xyz/') # create a TPB object with default domain
# Quick search for torrents, returns a Torrents object
torrents = t.search('public domain')

# See how many torrents were found
print('There were {0} torrents found.'.format(len(torrents)))

# Iterate through list of torrents and print info for Torrent object
for torrent in torrents:
    print(torrent)

# Customize your search
from tpblite import CATEGORIES, ORDERS
torrents = t.search('public domain', page=2, order=ORDERS.NAME.DES, category=CATEGORIES.VIDEO.MOVIES)

# Get the most seeded torrent based on a filter
torrent = torrents.getBestTorrent(min_seeds=30, min_filesize='500 MiB', max_filesize='4 GiB')

# Or select a particular torrent by indexing
torrent = torrents[3]

# Get the magnet link for a torrent
print(torrent.magnetlink)