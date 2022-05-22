from src.api.prj3.functions import *
from src.api.prj3.graph import Graph

import random
import numpy as np

graph = Graph()

<<<<<<< HEAD

def task1_2():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)


def task3():
    graph = Graph()
    create_and_draw_connected_graph_with_weight_dijkstra(graph, 8, 1)
    distance_matrix = np.empty([8, 8])
    graph.calculate_distance_matrix(distance_matrix)

    print(distance_matrix)

=======
def task1_2():
    print ("3.1: Generowanie spojnego grafu losowego")
    print ("3.2: Algorytm Dijkstry do znajdowania najkrotszych sciezek")
    #create_and_draw_connected_graph_with_weight_dijkstra(graph, nodes_number, start_node_for_dijkstra)
    create_and_draw_connected_graph_with_weight_dijkstra(graph,7,1)
    task3(graph,7)

# def task2():
   
#    create_and_draw_connected_graph_with_weight_dijkstra(graph,4,8)
   
   

def task3(graph, node_number):
    print("3.3: Macierz odleglosci miedzy wszystkimi wierzcholkami")
    #create_and_draw_connected_graph_with_weight(graph,4,8)
    distance_matrix = np.empty([node_number, node_number])
    graph.calculate_distance_matrix(distance_matrix)
   # distance_matrix
>>>>>>> 1e696cf (3.3 completed)

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
