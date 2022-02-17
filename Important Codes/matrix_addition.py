#matrix addition

import random as rd

r_lst=rd.sample(range(1,101), k=100)

dim=5

a=[rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5)]
b=[rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5),rd.sample(r_lst,k=5)]

c=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(dim):
	for j in range(dim):
		c[i][j]=a[i][j]+b[i][j]
print(c)