import re
import urllib
hand = urllib.urlopen('http://python-data.dr-chuck.net/regex_sum_371732.txt')
lst = []
for line in hand:
	line= line.rstrip()
	want = re.findall('[0-9]+' ,line)
	if len(want) ==0: continue
	#print want
	for i in want:
		num = float(i)
		lst.append(num)
	#print lst
	#print num
print sum(lst)	
