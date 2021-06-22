def stairs(h,m):
    if h==0:
        return 1
    ans=0
    for i in range(1,m+1):
        if (h-i)>=0:
            ans=ans+stairs(h-i,m)
    return ans
print(stairs(3,2))  


