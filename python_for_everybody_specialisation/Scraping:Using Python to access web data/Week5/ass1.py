import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url:')
url1 = urllib.urlopen(url).read()

tree = ET.fromstring(url1)
lst= []
lst1 = []
lst = tree.findall('comments/comment')
#print 'count:',len(lst)
for item in lst:
    #print 'Name',item.find('name').text
    lst1.append(int(item.find('count').text))
print sum(lst1)