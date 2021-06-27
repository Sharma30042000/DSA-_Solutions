def minword(l):
    k={}
    for i in l:
        s={}
        for j in i:
            if j not in s:
                s[j]=[j]
            else:
                s[j].append(j)
        for j in s:
            if j not in k:
                k[j]=s[j]
            else:
                if len(k[j])<len(s[j]):
                    k[j]=s[j]
    ans=[]
    for i in k:
        ans.extend(k[i])
    return ans

print(minword(["this","that","did","deed","them!","a"]))

