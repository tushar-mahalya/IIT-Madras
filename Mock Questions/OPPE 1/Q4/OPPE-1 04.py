x=input().split(",")
lst=[]
for i in x:
	lst.append(int(i))
mid=int(len(lst)/2)
lhs=sum(lst[:mid])
rhs=sum(lst[mid:])
if(lhs==rhs):
	print("balanced")
elif(lhs>rhs):
	print("left-heavy")
elif(lhs<rhs):
	print("right-heavy") 
