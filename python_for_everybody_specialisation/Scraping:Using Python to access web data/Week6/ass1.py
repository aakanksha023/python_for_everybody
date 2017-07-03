import json
import urllib
lst =[]
num=[]
url = raw_input('Enter Url:')
url1 = urllib.urlopen(url).read()
#print url1
info = json.loads(url1)
info1 = info.values()
info2 = info1[1]
for i in info2:
	lst.append(i.values())
#print lst
for x in lst:
	num.append(x[0])
print sum(num)    	

	 

		