from turtle import distance
from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.parse_input import parse_input
from src.api.prj1.generate_random_graph import generate_with_edge_count, generate_with_probability
from src.api.prj1.conversions import *
from src.api.prj3.functions import *
from src.api.prj3.graph import Graph
import random 
import numpy as np

graph = Graph()

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
    
    print(distance_matrix)
    task4(graph,node_number,distance_matrix)
    # distance_matrix

def task4(graph,node_number,distance_matrix):
    print("3.4: Wyznaczenie centrum grafu")
    graph_center(distance_matrix)
    minimax(distance_matrix)
    graph.draw_graph_with_weight()

    task5(graph)

def task5(graph):
    print("3.5: Wyznaczenie minimalnego drzewa rozpinajacego")
    graph.prim_algorithm()
    

    

    