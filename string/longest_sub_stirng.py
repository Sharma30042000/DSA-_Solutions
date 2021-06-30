def helper(s,i):
    if i<len(s)//2:
        f=s[i]
        k=""
        for j in range(1,i+1):
            if s[i-j]==s[i+j]:
                f=s[i-j]+f+s[i+j]
            else:
                break
        if s[i]==s[i+1]:
            k=s[i]+s[i+1]
            for j in range(1,i+1):
                if s[i-j]==s[i+1+j]:
                  k=s[i-j]+k+s[i+1+j]
                else:
                   break
        if len(f)>len(k):
            return f
        else:
            return k   
    if i>=len(s)//2:
        f=s[i]
        k=""
        for j in range(1,len(s)-i):
            if s[i-j]==s[i+j]:
                f=s[i-j]+f+s[i+j]
            else:
                break
        if s[i]==s[i+1]:
            k=s[i]+s[i+1]
            for j in range(1,len(s)-i-1):
                if s[i-j]==s[i+j+1]:
                    k=s[i-j]+k+s[i+j+1]
                else:
                    break
        if len(f)>len(k):
            return f
        else:
            return k
def ls(s):
    if len(s)<2:
        return s
    ans=""
    for i in range(0,len(s)-1):
        f=helper(s,i)
        if len(f)>len(ans):
            ans=f
    return ans
print(ls("aabbaa"))
           




           