import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre
''' )

cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

cur.executescript('''

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)''')


cur.executescript(''' 
	CREATE TABLE Genre ( 
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
)''')

cur.executescript('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

def advanced_lookup(ele, list_of_tag):
    lst = []
    for x in list_of_tag:
        y = lookup(ele,x)
        lst.append(y)
    return lst     

def find_the_index(ele, list_1):
    y = None
    for x in range(len(list_1)):
        if list_1[x]  == ele:
            y = x
    return y

def efficient_lookup(ele, input_list):
    dup_list = range(len(input_list))
    found = False
    for x in ele:
        if found:
            dup_list[m] = x.text
            found = False
        if x.tag == 'key' and x.text in input_list:
            m = find_the_index(x.text, input_list)
            found = True            
    return dup_list

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
#print type(all[0])
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    # name = lookup(entry, 'Name')
    # artist = lookup(entry, 'Artist')
    # album = lookup(entry, 'Album')
    # count = lookup(entry, 'Play Count')
    # rating = lookup(entry, 'Rating')
    # length = lookup(entry, 'Total Time')
    # genre = lookup(entry, 'Genre')

    input_list = ['Name','Artist','Album','Play Count','Rating','Total Time','Genre']
    # output_list = advanced_lookup(entry, input_list)
    output_list = efficient_lookup(entry, input_list)
    print 'Output List',output_list

    # if name is None or artist is None or album is None or genre is None : 
    #     continue

    # #print name, " -- ", artist, " -- ", album, " -- ", genre

    # cur.execute('''INSERT OR IGNORE INTO Artist (name) 
    #     VALUES ( ? )''', ( artist, ) )
    # cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    # artist_id = cur.fetchone()[0]
    # #print type(cur.fetchone())

    # cur.execute('''INSERT OR IGNORE INTO Genre (name) 
    #     VALUES ( ? )''', ( genre, ) )
    # cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # genre_id = cur.fetchone()[0]


    # cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
    #     VALUES ( ?, ? )''', ( album, artist_id ) )
    # cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    # album_id = cur.fetchone()[0]

    # cur.execute('''INSERT OR REPLACE INTO Track
    #     (title, album_id, len, rating, count, genre_id) 
    #     VALUES ( ?, ?, ?, ?, ? ,?)''', 
    #     ( name, album_id, length, rating, count, genre_id ) )

    # conn.commit()
