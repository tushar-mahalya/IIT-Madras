#Birthday Pardox

import random as rd

l =[]
for i in range(50):
	l.append(rd.randint(1,365))
l.sort()
print(l) 
#initiation of list with random variables competed 

i=0
flag=1
while (i<len(l)-1):
    	if (l[i]==l[i+1]):
    		print("Repetion", l[i], l[i+1])
    		flag=1
    	i=i+1
if flag==0:
	print("No Repetition")