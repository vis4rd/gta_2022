def LsMs(matrix):
    rows, cols = (len(matrix), len(matrix))
    Ms = [[0 for i in range(cols)] for j in range(rows)]
    i=0
    j=0
    for w in matrix:
        for k in w:
            i=0
            while i!=k-1:
                i=i+1
            Ms[j][i]=1
        j=j+1
    return Ms