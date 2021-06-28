def hash(s):
    k={}
    for i in s:
        if i not in k:
            k[i]=1
        else:
            k[i]=k[i]+1
    return k
def smallsub(s,sub):
    h2=hash(sub)
    k={}
    i=0
    l=0
    st=0
    final=[0,len(s)]
    while i<len(s):
        if s[i] in h2 and l<len(sub):
            if s[i] in k:
                k[s[i]]=k[s[i]]+1
            else:
                k[s[i]]=1
            if k[s[i]]<=h2[s[i]]:
                l=l+1
        if l==len(sub):
            if (final[1]-final[0])>=(i-st):
                final[0]=st
                final[1]=i
            if s[st] in h2:
                k[s[st]]=k[s[st]]-1
                if k[s[st]]<h2[s[st]]:
                    l=l-1
                    i=i+1
                st=st+1
                continue
            if s[st] not in h2:
                st=st+1
                continue
        i=i+1
    return s[final[0]:final[1]+1]
print(smallsub("aabcd$ef$axb$c$","$$abf"))
