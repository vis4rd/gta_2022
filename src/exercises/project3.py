from turtle import distance
from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.parse_input import parse_input
from src.api.prj1.generate_random_graph import generate_with_edge_count, generate_with_probability
from src.api.prj1.conversions import *
import random 
import numpy as np


def task1():
    print ("3.1: Generowanie spojnego grafu losowego")
    create_and_draw_connected_graph_with_weight(graph,4,8)


def task2():
   print ("3.2: Algorytm Dijkstry do znajdowania najkrotszych sciezek")
   create_and_draw_connected_graph_with_weight(graph,4,8)
   
   s=random.randint(0,len(graph.nodes)-1)
   d = [], p = []
   
   graph.dijkstra_algorithm(p,d,s)

def task3():
    print("3.3: Macierz odleglosci miedzy wszystkimi wierzcholkami")
    create_and_draw_connected_graph_with_weight(graph,4,8)
    distance_matrix = {}
    graph.calculate_distance_matrix(distance_matrix)
    np.print_matrix(distance_matrix)

def task4():
    print("3.4: Wyznaczenie centrum grafu")
    create_and_draw_connected_graph_with_weight(graph,4,8)

def task5():
    print("3.5: Wyznaczenie minimalnego drzewa rozpinajacego")
    create_and_draw_connected_graph_with_weight(graph,4,8)
    graph.print_edges()
    minimum_spanning_tree(graph)

    