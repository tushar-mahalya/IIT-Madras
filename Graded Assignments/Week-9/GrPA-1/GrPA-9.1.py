def get_freq(filename): 
    f=open(filename,'r') 
    d={} 
    s=f.readlines() 
    for i in s: 
        if i!=s[-1]: 
            i=i[:-1] 
            if i not in d: 
                d[i]=1 
            else: 
                d[i]+=1 
        else: 
            if i not in d: 
                d[i]=1 
            else: 
                d[i]+=1 
    f.close() 
    return d
