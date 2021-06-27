def duplication(s):
    k={}
    st=0
    t=[0,0]
    for i in range(len(s)):
        if s[i] in k:
            if (t[1]-t[0]) < (i-st):
                t[0]=st
                t[1]=i
            st=max(st,k[s[i]]+1)
        k[s[i]]=i
    return s[t[0]:t[1]]

print(duplication("clementisacap"))

        
