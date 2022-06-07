from ..prj3.graph import *


def generate_and_draw_digraph_with_weight(graph, l1, l2, p):
    graph.generate_random_digraph(l1, l2, p)
    graph.add_random_weight()
    graph.draw_di_graph_with_weight()
