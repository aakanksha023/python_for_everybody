def is_present_in(ele,to_check_list):
	y= False
	for x in to_check_list:
		if x == ele:
			y = True
	return y	

a = [1,2,3,4,5,6,10,1,2,3]
b = [10,1,6,5,7,8]

#print is_present_in(10,b)

def count_of(ele, to_check_list):
	count = 0
	for x in to_check_list:
		if x == ele:
			count = count + 1
	return count		
#print count_of(10,b)	

def common(list_1,list_2):
	lst = []
	for x in list_1:
		if is_present_in(x,list_2):
			lst.append(x)
	return lst		

#print common(a,b)	

def union(list_1,list_2):
	lst = list_1
	for x in list_2:
		if x in lst: continue
		else:
			lst.append(x)
	return lst		
#print union(a,b)


def union1(list_1,list_2):
	lst = list_1
	for x in list_2:
		if x not in lst:
			lst.append(x)
	return lst	
	
#print union1(a,b)		


def unique(list_1):
	lst = []
	for x in list_1:
		if x not in lst:
			lst.append(x)
	return lst
	
#print unique(a)

def find_the_index(ele, list_1):
	y = None
	for x in range(len(list_1)):
		if list_1[x]  == ele:
			y = x
	return y			



