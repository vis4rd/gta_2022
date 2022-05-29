from src.api.prj3.functions import *
from src.api.prj3.graph import Graph
from src.api.prj4.functions import *
import random

def proj_4():
    print("--- Kosaraju ---")
    graph = Graph()
    generate_and_draw_digraph_with_weight(graph, 4, 4, 0.6)
    print(graph.kosaraju())

    print("--- Bellman-Ford ---")
    generate_and_draw_digraph_with_weight(graph, 4, 5, 0.5)
    print(graph.bellman_ford(graph.nodes[0].number))

    print('--- Johnson ---')
    generate_and_draw_digraph_with_weight(graph, 4, 5, 0.5)
    print(graph.johnson())