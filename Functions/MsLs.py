def MsLs(matrix):
    Ls=[]
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix)):
            if matrix[r][c]==1:
                row.append(c+1)
        Ls.append(row)
    
    return Ls
        