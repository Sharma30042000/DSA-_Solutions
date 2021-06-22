def phone(n):
    if len(n)==1 and int(n)<2:
        return n
    if len(n)==1 and int(n)>=2:
        if int(n)<=6 :
            f=97+(int(n)-2)*3
            return [chr(f),chr(f+1),chr(f+2)]
        if int(n)==7:
            return ["p","q","r","s"]
        if int(n)==8:
            return ["t","u","v"]
        if int(n)==9:
            return ["w","x","y","z"]
    ans=[]  
    for j in phone(n[0]):
            s=0
            for k in phone(n[1:]):              
                s=j+k
                ans.append(s)  
    return ans
print(phone("1905"))