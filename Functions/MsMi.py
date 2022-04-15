def MsMi(matrix):
    root=0
    i=0
    for w in matrix:
        for el in w[i+1:]:
            if el==1:
                root+=1
        i+=1
    cols, rows = (root,len(matrix))
    Mi = [[0 for i in range(cols)] for j in range(rows)]
    i=0
    r=0
    for w in matrix:
        j=i+1
        for el in w[i+1:]:
            if el==1:
                Mi[j][r]=1
                Mi[i][r]=1
                r+=1
            j+=1
        i+=1
    return Mi

        
