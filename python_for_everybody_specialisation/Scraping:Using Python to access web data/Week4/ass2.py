import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
reps = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
 #   print tag.get('href', None)
#print url
for i in range(reps):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print url   