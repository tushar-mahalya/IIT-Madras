y=input()
x=list(y)
count=0
for i in range(len(x)):
	if x[i] in "lo":
		count += 1
if (count !=0):
	print(count,"mistakes")
else:
	print("No mistakes")

if(count>0):
    a=y.replace("l", "1")
    b=int(a.replace("o", "0"))
    print(b)
