from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.parse_input import parse_input
from src.api.prj1.generate_random_graph import generate_with_edge_count, generate_with_probability
from src.api.prj1.conversions import *

def task1():
    adj_list = []
    with open('data_1.txt', 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
        adj_list = parse_input(l)
    
    print("Adjacency list:")
    for row in adj_list:
        for el in row:
            print(el, end=' ')
        print()
    print()

    print("Adjacency matrix:")
    for row in convert_adj_list_to_adj_matrix(adj_list):
        for el in row:
            print(el, end=' ')
        print()
    print()

    print("Incidence matrix:")
    for row in convert_adj_list_to_inc_matrix(adj_list):
        for el in row:
            print(el, end=' ')
        print()
    print()

def task2():
    adj_list = []
    with open('data_1.txt', 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
        adj_list = parse_input(l)
    draw_graph(adj_list)

def task3():
    adj_list = generate_with_edge_count(10, 46)
    draw_graph(adj_list)

    adj_list = generate_with_probability(9, 0.5)
    draw_graph(adj_list)
