#checking a random number in a list

import random as rd
l=[]
for i in range(1000):
	l.append(rd.randint(1,8000))

flag=0
val=0

while (val>-1):
	print("Enter a number, type -1 to exit")
	val=int(input())
	for i in range(len(l)):
		if (val==l[i]):
			print("Yes it exist")
			flag=1
			break
	if (flag==0):
		print("Doesn't Exist")
		