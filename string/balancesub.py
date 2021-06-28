def balance(s):
    k=[]
    ans=0
    st=0
    for i in range(len(s)):
        if s[i]=="(":
            k.append([s[i],i])
        else:
            if len(k)>0:
                if k[-1][0]=="(":
                    k.pop(-1)
                else:
                    k.append([s[i],i])
            else:
                k.append([s[i],i])
    for i in k:
        if i[1]-st>=ans:
            ans=i[1]-st
        st=i[1]+1
    return max(ans,len(s[st:]))
            
print(balance("()()))))()()("))
