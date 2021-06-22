def GenerateDiv(n,s,e,st,f):
    if s==0 and e==0:
        f.append(st)
        return f
    if s>0:  
         GenerateDiv(n,s-1,e,st+"[",f)
    if e>s:
        GenerateDiv(n,s,e-1,st+"]",f)    
    return f
print(GenerateDiv(3,3,3,"",[]))
