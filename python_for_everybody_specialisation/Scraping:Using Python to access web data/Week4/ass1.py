import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

	#Retrieve all of the span tags
tags = soup('span')
num2= []
num3= []
for tag in tags:
   num1 = 'Contents:',tag.contents[0]
   for x in num1:
   	num2 = int(num1[1])
   num3.append(num2)
print sum(num3)