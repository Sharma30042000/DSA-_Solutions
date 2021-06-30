def inter(A):
    temp=A[0]
    ans=A[0]
    for k in range(1,len(A)):
        i=A[k]
        if i>=0:
            if temp<0:
                temp=i
                if ans<temp:
                    ans=temp                
            else:
                temp=temp+i
                if ans<temp:
                    ans=temp
        else:
            if temp<0 and temp<=i:
                temp=i
                if ans<temp:
                    ans=temp
            if temp>0 and temp+i<=0:
                if ans<temp:
                    ans=temp
                temp=0
            if temp>0 and temp+i>0:
                if ans<temp:
                    ans=temp
                temp=temp+i

    return ans            





print(inter([-3,-3,-3,-3,-3]))