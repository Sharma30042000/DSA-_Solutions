def SparseMatrixMultiplication(a1,b1):
    if len(a1[0])!=len(b1):
        return [[]]
    for i in len(a1):
        c=0
        for j in len(b1[0]):
            if a1[i][c]==0 or b1[c][j]==0:
                c=c+1
            else:
                