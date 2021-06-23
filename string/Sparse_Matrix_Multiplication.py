def SparseMatrixMultiplication(a1,b1):
    if len(a1[0])!=len(b1):
        return [[]]
    mat=[]
    for i in range(len(a1)):
            mat.append([])
            
    for i in range(len(a1)):
        for j in range(len(b1[0])):
            s=0
            for k in range(len(b1)):
                if a1[i][k]==0 or b1[k][j]==0:
                    s=s
                else:
                    s=s+a1[i][k]*b1[k][j]
            mat[i].append(s)
    return mat
print(SparseMatrixMultiplication([[0,2,0],[0,-3,5]],[[0,10,0],[0,0,0],[0,0,4]]))        

