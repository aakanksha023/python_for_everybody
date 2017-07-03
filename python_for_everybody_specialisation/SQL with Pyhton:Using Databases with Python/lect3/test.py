import xml.etree.ElementTree as ET
import sys
import sqlite3
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
a = all[0]
for x in range(len(a)):
    if x <(len(a)-1):
        if x % 2 !=0:
            sys.stdout.write(str(a[x].text)+'\n')
        else:
            sys.stdout.write(str(a[x].text)+ ',')
    else:
        sys.stdout.write(str(a[x].text)+ '\n' )    
    # if x.tag == 'key':
    #     print 'Tag is',x.text 

#print type(all[0])
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : continue

#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
#     genre = lookup(entry, 'Genre')