def helper(s,i):
    if i<len(s)//2 and s[i]==s[i+1]:
         f=s[i]+s[i+1]
         if i==1 and s[0]==s[3]:
             return s[0]+f+s[3]
         if i==1 and s[0]==s[2]:
             return s[0]+f
         if i==2 and s[0]==s[4] and s[1]==s[3]:
             return s[0]+s[1]+f+s[4]
         for j in range(1,i+1):
             if s[i-j]==s[i+1+j]:
                 f=s[i-j]+f+s[i+1+j]
             else:
                 return f    
         return f
    if i<len(s)//2:
        f=s[i]
        for j in range(1,i+1):
            if s[i-j]==s[i+j]:
                f=s[i-j]+f+s[i+j]
            else:
                return f    
        return f    
    if i>=len(s)//2 and s[i]==s[i+1]:
        f=s[i]+s[i+1]
        if i==len(s)-2 and s[i-1]==s[i+1]:
            return s[i-1]+f
        for j in range(1,len(s)-i-1):
            if s[i-j]==s[i+j+1]:
                f=s[i-j]+f+s[i+j+1]
            else:
                return f
        return f
    if i>=len(s)//2:
        f=s[i]
        for j in range(1,len(s)-i):
            if s[i-j]==s[i+j]:
                f=s[i-j]+f+s[i+j]
            else:
                return f
        return f
def ls(s):
    if len(s)<2:
        return s
    if len(s)==2 and s[0]==s[1]:
        return s
    ans=""
    for i in range(1,len(s)-1):
        f=helper(s,i)
        if len(f)>len(ans):
            ans=f
    return ans
print(ls("aaaaabaegrffkdcc"))
           




           