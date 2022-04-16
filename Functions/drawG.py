import networkx as nx
import matplotlib.pyplot as plt

def DrawGraph(matrix):

    graph = nx.DiGraph()

    node_neighbors = [ ]
    current_node = 1
    for neighbors in matrix:
        for neighbor in neighbors:
            node_neighbors.append((current_node, neighbor))
        current_node += 1
    
    graph.add_edges_from(node_neighbors)
    # nx.draw_networkx(G=graph, pos=nx.circular_layout(graph), with_labels=True)
    # nx.draw(graph, pos=nx.circular_layout(G=graph, dim=2))
    nx.draw_circular(G=graph, with_labels=True, arrowstyle="-")
    plt.show()

    # info: nx rysuje node'y w zlej kolejnosci wiec pewnie recznie trzeba
    # najpierw dodac node'y, a potem wszystkie edge
