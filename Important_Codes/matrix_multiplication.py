#matrix_multiplication

import random as rd

l=rd.sample(range(1,101), k=100)

dim = 4

A = [rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4)]
B = [rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4),rd.sample(l,k=4)]

C = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(dim):
	for j in range(dim):
		for k in range(dim):
			C[i][j] = C[i][j] + A[i][k] + B[k][j]
print(C)