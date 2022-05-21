from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.generate_random_graph import generate_with_edge_count
from src.api.prj2.graphic_sequence import *
from src.api.prj2.maximal_connected_subgraph import maximal_connected_subgraph, all_connected_subgraphs
from src.api.prj2.euler_graph import generate_euler_graph
from src.api.prj2.k_regular_graph import generate_k_regular_graph

def task1():
    sequence = []
    with open('data_2.txt', 'r') as f:
        sequence = [int(num) for num in f.readline().split(' ')]
    
    is_gseq = is_graphic_sequence(sequence)
    print(is_gseq)

    if is_gseq:
        adj_list = generate_with_graphic_sequence(sequence)
        draw_graph(adj_list)

def task2():
    sequence = []
    with open('data_2.txt', 'r') as f:
        sequence = [int(num) for num in f.readline().split(' ')]

    is_gseq = is_graphic_sequence(sequence)
    print(is_gseq)

    if is_gseq:
        adj_list = generate_simple_graph_with_graphic_sequence(sequence, 10)
        draw_graph(adj_list)

def task3():
    adj_list = generate_with_edge_count(10, 5)

    mcs = maximal_connected_subgraph(adj_list)
    print(mcs)

    # PRINT ALL SUBGRAPHS FOR SHOWCASE
    # all = all_connected_subgraphs(adj_list)
    # for row in all:
    #     for el in row:
    #         print(el, end=" ")
    #     print()

    draw_graph(adj_list)

def task4():
    adj_list = generate_euler_graph(5)

    draw_graph(adj_list)

def task5():
    adj_list = generate_k_regular_graph(20, 6)

    draw_graph(adj_list)
