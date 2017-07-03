import json
import urllib
num = []
url = raw_input('Enter Url:')
url1 = urllib.urlopen(url).read()
#print url1
js = json.loads(str(url1))
#print type(js)
#print len(js['comments'])
#print json.dumps(js, indent=4)
for x in range(50):
	count1 = js["comments"][x]["count"]
	num.append(count1)
print sum(num)	  