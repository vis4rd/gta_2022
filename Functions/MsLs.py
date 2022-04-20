# Macierz sasiedztwa zamiana do listy sasiedztwa
def MsLs(matrix):
    Ls=[]

    # r - zmienna operujaca na wierszach , c - zmienna operujaca na kolumnach 
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix)):
            # jezeli element macierzy jest doddatni (=1) to dodajemy numer sasiada do listy  
            if matrix[r][c]==1:
                row.append(c+1)
        Ls.append(row)
    
    return Ls
        