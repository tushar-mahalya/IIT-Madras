# program for doing obvious sort (without using predefined sort meathod)

import random as rd
l=[]
for i in range(50):
	l.append(rd.randint(1,100))
print(l)

x=[]

while (len(l)>0):
	min=l[0]
	for i in range(len(l)):
		if (l[i]<min):
			min=l[i]
	x.append(min)
	l.remove(min)
print(x)
	