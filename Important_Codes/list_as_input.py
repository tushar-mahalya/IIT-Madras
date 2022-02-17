#for accepting list as input

l = input("Enter a list of numbers: ").split(' ')
lis=[]
for i in l:
	lis.append(int(i))
print(lis)