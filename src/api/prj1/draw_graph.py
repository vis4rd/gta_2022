# Rysowanie grafu
import networkx as nx
import matplotlib.pyplot as plt

# rotation operation on array:
# impl_RotateArray([1, 2, 3, 4, 5], 2, 5) = [3, 4, 5, 1, 2]
def _RotateArray(array, step, size):
    array[:] = array[step:size] + array[0:step]
    return array

def _ReverseArray(array):
    return array[::-1]

def DrawGraph(matrix):
    # Order of nodes depends on order of them in the array, ThErE iS nO oThEr WaY.
    # Firstly, networkx supports only counter-clockwise order of drawing (very sad times),
    #     so the order in the array has to be reversed.
    # Additionally, drawing begins in the east side instead of the north side,
    #     so the array has to be rotated.

    node_count = len(matrix)
    nodes = [i for i in range(1, node_count+1)]
    nodes = _ReverseArray(nodes)
    nodes = _RotateArray(nodes, -(int(node_count/4) + 1), node_count) # start from north instead of east

    edges = [ ]
    current_node = 1
    for neighbors in matrix:
        for neighbor in neighbors:
            edges.append((current_node, neighbor))
        current_node += 1
    
    # nx.draw_networkx(G=graph, pos=nx.circular_layout(graph), with_labels=True)
    # nx.draw(graph, pos=nx.circular_layout(G=graph, dim=2))
    # nx.draw_circular(G=graph, with_labels=True, arrowstyle="-")
    
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    nodes_pos = nx.circular_layout(graph)
    nx.draw(G=graph, with_labels=True, arrowstyle="-", pos=nodes_pos)
    plt.show()
