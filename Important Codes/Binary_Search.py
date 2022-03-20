'''binary search'''
def binary(L,k):
    first=0
    last=len(L)-1
    while (last-first>1):
        mid=(last-first)//2
        if (L[mid]==k):
            return 1
        if (L[mid]>k):
            last=mid-1
        if (L[mid]<k):
            first=mid+1
    if (L[first]==k) or (L[last]==k):
        return 1
    else:
        return 0

l=[12,34,56,78,13,65,98]
print(binary(l,7))
    
