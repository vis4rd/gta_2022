
from graph import *


def create_and_draw_connected_graph_with_weight(graph, l1, l2):
    graph.generate_random_connected_graph(l1, l2)
    graph.add_random_weight()
    graph.draw_graph_with_weight()