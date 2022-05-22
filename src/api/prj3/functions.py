
from turtle import distance
from graph import *


def create_and_draw_connected_graph_with_weight(graph, nodes_number):
    graph.generate_random_connected_graph(nodes_number)
    graph.add_random_weight()
    graph.draw_graph_with_weight()

def create_and_draw_connected_graph_with_weight_dijkstra(graph, nodes_number, s):
    graph.generate_random_connected_graph(nodes_number)
    graph.add_random_weight()

    if s>nodes_number-1:
        s=nodes_number-1
   
    d = []
    p = []
    
    graph.dijkstra_algorithm(p,d,s)

    graph.draw_graph_with_weight()

def print_node_set(S,d,p):
    print (f'START: S = {S[0]}')
    
    for i in S:
        print(f'd({i}) = {d[i]} ==> [', end='')
        indx = i
        path = None
        path = [indx]
        prev_indx = p[indx]
        while prev_indx is not None:
            path.append(prev_indx)
            indx= prev_indx
            prev_indx = p[indx]
        
        for node in reversed(path):
            if node == path[0]:
                print(f' {node} ]' )       
            else:
                print(f' {node} -', end ='')


def node_with_smallest_d(S,d):
    min_distance = float('inf')
    node = None
    for i, temp_distance in enumerate(d):
        if i not in S:
            if min_distance > temp_distance:
                node = i 
                min_distance = temp_distance
    return node



    
