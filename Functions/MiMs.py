# Macierz incydencji zamiana do macierzy sasiedztwa 
def MiMs(matrix):

    rows, cols = (len(matrix), len(matrix))
    Ms = [[0 for i in range(cols)] for j in range(rows)]
    first = -1
    for c in range(len(matrix[0])):
        for w in range(len(matrix)):
            if matrix[w][c]==1:
                if first>=0:
                    Ms[first][w]=1
                    first=-1
                else:
                    first=w
    diag = 1
    for w in range(len(matrix)):
        for c in range(diag,len(matrix)):
            Ms[c][w]=Ms[w][c]
        diag+=1
        
    return Ms
