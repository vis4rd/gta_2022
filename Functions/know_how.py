import imp
from xmlrpc.client import boolean
from .MiMs import MiMs
from .MsLs import MsLs
from .LsMs import LsMs
from .MsMi import MsMi
from .drawG import DrawGraph

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


def Mi(matrix):
    print(" I AM MI")
    Ms=MiMs(matrix)
    Ls=MsLs(Ms)
    write(Ms,Ls,matrix)

def Ls(matrix):
    print(" I AM LS")
    Ms = LsMs(matrix)
    Mi = MsMi(Ms)
    write(Ms,matrix,Mi)

def Ms(matrix):
    print("I AM MS")
    Ls=MsLs(matrix)
    Mi=MsMi(matrix)
    write(matrix,Ls,Mi)
    DrawGraph(Ls)


def recognize(matrix):
    i = len(matrix)
    j = len(matrix[0])
    iequalsj = True
    for tab in matrix:
        if j != len(tab):
            Ls(matrix)
            iequalsj = False
            break
        j=len(tab)
    if i == j:
        Ms(matrix)
    elif iequalsj==True:
        Mi(matrix)

        

        