# Lista sasiedztwa zamiana do macierzy sasiedztwa
def LsMs(matrix):

    # tworzymy macierz i zerujemy, wymiary uzyskane na podstawie dlugosci (ilosci wierszy) listy sasiedztwa
    rows, cols = (len(matrix), len(matrix))
    Ms = [[0 for i in range(cols)] for j in range(rows)]

    i=0
    j=0

    # zakladamy ze kolejnosc wierszy w pliku odpowiada odpowiada kolejnosci wezlow, tj. 1 wiersz opisuje sasiadow pierwszego wiersza
    # pobieramy wiersze
    for row in matrix:

        # pobieramy kolejne numery sasiada z wiersza listy sasiedztwa
        for neighbor_number in row:
            Ms[j][neighbor_number-1]=1

        j=j+1
    return Ms