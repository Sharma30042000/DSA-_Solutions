def maxArr(A):
        m=max(A)
        mi=min(A)
        im=A.index(m)
        imi=A.index(mi)
        print(im,imi)
        A.sort()
        print(A)
        if m==mi:
            return abs(len(A)-1)
        else:
            return abs(m-mi)+abs(im-imi)
print(maxArr([55,-8,43,52,8,59,-91,-79,-18,-94]))