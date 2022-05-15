from matplotlib.pyplot import draw
from src.api.prj1.draw_graph import draw_graph
from src.api.prj2.graphic_sequence import *

def task1():
    sequence = []
    with open('data_2.txt', 'r') as f:
        sequence = [int(num) for num in f.readline().split(' ')]
    
    is_gseq = is_graphic_sequence(sequence)
    print(is_gseq)
    adj_list = generate_with_graphic_sequence(sequence)
    draw_graph(adj_list)

    adj_list = generate_simple_graph_with_graphic_sequence(sequence, 10)
    draw_graph(adj_list)
