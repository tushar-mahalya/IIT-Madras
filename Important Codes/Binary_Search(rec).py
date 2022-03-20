'''binary search recursive way'''
def rbinary(L,k,f,l):
    if (len(L)==0):
        return 0
    if (f==l):
        if (k==L[f]):
            return 1
        else:
            return 0
    if (l-f==1):
        if (L[f]==k) or (L[l]==k):
            return 1
        else:
            return 0
    if (l-f>1):
        m = (l-f)//2
        if (L[m]>k):
            l=m-1
        if (L[m]<k):
            f=m+1
        if (L[m]==k):
            return 1
    return rbinary(L,k,f,l)


l=[12,34,56,78,13,65,98]
print(rbinary(l,12,0,len(l)-1))




