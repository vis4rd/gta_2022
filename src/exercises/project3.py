from src.api.prj3.functions import *
from src.api.prj3.graph import Graph

import random
import numpy as np

graph = Graph()


def task1_2():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)


def task3():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)
    distance_matrix = np.empty([8, 8])
    graph.calculate_distance_matrix(distance_matrix)

    print(distance_matrix)


def task4():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)

    distance_matrix = np.empty([8, 8])
    graph.calculate_distance_matrix(distance_matrix)

    graph_center(distance_matrix)
    minimax(distance_matrix)


def task5():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)

    graph.prim_algorithm()
    graph.draw_graph_with_weight()
