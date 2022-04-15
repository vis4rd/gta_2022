import networkx as nx
import matplotlib.pyplot as plt

def DrawGraph(matrix):

    G = nx.DiGraph()
    for r in matrix:
        for c in r:
            G.add_edges_from([r+1,c+1])