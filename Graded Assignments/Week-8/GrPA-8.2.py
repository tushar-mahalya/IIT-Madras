def linear (P, Q, k):
    if len(P) != len(Q):
        return False 
    if len(P)==1:
        if P[0]/Q[0]==k: 
            return True 
        else: 
            return False 
    else:
        if P[0]/Q[0]==k:
            return linear (P[1:],Q[1:],k)
        else:
            return False