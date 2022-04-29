# from xmlrpc.client import boolean
from .MiMs import MiMs
from .MsLs import MsLs
from .LsMs import LsMs
from .MsMi import MsMi
from .draw_graph import DrawGraph

def ListW(file, List):
    for r in List:
        for c in r:
            file.write(str(c)+" ")
        file.write("\n")

def write(Ms, Ls, Mi):
    with open("Ms.txt","w") as ms:
        ListW(ms,Ms)
    with open("Ls.txt","w") as ms:
        ListW(ms,Ls)
    with open("Mi.txt","w") as ms:
        ListW(ms,Mi)

# Mi - macierz incydencji
def Mi(matrix):
    print(" I AM MI")
    Ms=MiMs(matrix)
    Ls=MsLs(Ms)
    write(Ms,Ls,matrix)
    DrawGraph(Ls)


# Ls - lista sasiedztwa 
def Ls(matrix):
    print(" I AM LS")
    Ms = LsMs(matrix)
    Mi = MsMi(Ms)
    write(Ms,matrix,Mi)
    DrawGraph(Ls)


# Ms - macierz sasiedztwa
def Ms(matrix):
    print("I AM MS")
    Ls=MsLs(matrix)
    Mi=MsMi(matrix)
    write(matrix,Ls,Mi)
    DrawGraph(Ls)


def recognize(matrix):
    
    #ilosc wierszy 
    row_number = len(matrix)
    #ilosc kolumn w wierszu
    column_number = len(matrix[0])
    
 

    #petla sprawdzajaca ilosc elementow w wierszu
    for single_row in matrix:

        #jezeli nie jest prostokatna to jest to lista incydencji 
        if column_number != len(single_row):
            Ls(matrix)
            return

    #jezeli kwadratowa to macierz sasiedztwa 
    if row_number == column_number:
        Ms(matrix)

    #jezeli nie to macierz incydencji 
    else:
        Mi(matrix)

        

        