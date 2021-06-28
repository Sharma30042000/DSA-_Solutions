def underscore(s,sub):
    l=list(s.split(" "))
    print(l)
    ans=""
    for i in l:
        if len(i)<len(sub):
            ans=ans+i+" "
        if len(i)>len(sub):
            if i[0:len(sub)]==sub and i[-len(sub):]!=sub:
                ans=ans+"_"+sub+"_"+i[len(sub):]+" "
            elif i[-len(sub):]==sub and i[0:len(sub)]!=sub:
                ans=ans+i[0:len(i)-len(sub)]+"_"+sub+"_"+" "
            elif i[0:len(sub)]==sub and i[-len(sub):]==sub:\
                ans=ans+"_"+i+"_"+" "
            else:
                ans=ans+i+" "
     
    return ans[0:len(ans)-1]
print(underscore("testthis is a testtest to see if testestest it works","test"))
