def reverse(s):
    l=[]
    k=""
    for i in s:
        if i==chr(32) and k!=0:
            l.append(k)
            l.append(i)
            k=""
        elif i==chr(32):
            l.append(i)      
        else:
            k=k+i
    l.append(k)
    ans=""
    for j in range(len(l)):
        ans=ans+l.pop(-1)
    return ans
print(reverse("demo is the best!"))
print(reverse("4  whitespace"))
