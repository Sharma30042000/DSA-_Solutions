def  dtree(n,l,r):
    if l==1 and r==1:
        return 1
    if l==0 and r==1:
        return 1
    if r==0 and l==1:
        return 1
    s=0 
    if l>1:
        for x in range(0,l):
            s=s+dtree(l,x,l-1-x)
    if r>1:
        for x in range(0,r):
            s=s+dtree(r,x,r-1-x)
    if l==-1 and r==-1:
        for x in range(0,n):
            s=s+dtree(n,x,n-1-x)
    return s
print(dtree(4,-1,-1))