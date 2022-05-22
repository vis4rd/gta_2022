import random
import logging as log

from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.generate_random_graph import generate_with_probability
from src.api.prj1.conversions import convert_adj_list_to_adj_matrix
from src.api.prj2.graphic_sequence import generate_with_graphic_sequence, _edge_count

def generate_euler_graph(node_count):
    if node_count < 3:
        log.info(f"node_count({node_count}) < 3, setting it to 3")
        node_count = 3

    graph_adj_list = [[] for _ in range(node_count)]
    while not _is_eulerian(graph_adj_list):
        graph_adj_list = generate_with_probability(node_count, 0.6)
        log.debug(f"adj_list = {graph_adj_list}")

    return graph_adj_list


def _is_eulerian(adj_list) -> bool:
    log.debug(f"adj_list = {adj_list}")
    for node in adj_list:
        if (len(node) <= 0) or (len(node)%2 != 0):
            log.debug("Graph is not eulerian")
            return False
    log.debug("Graph is eulerian")
    return True


def find_eulerian_path(adj_list):
    adj_matrix = convert_adj_list_to_adj_matrix(adj_list)
    node_count = len(adj_list)

    nodes_degrees = []
    for i in range(node_count):
        nodes_degrees.append(sum(adj_matrix[i]))
  
    startpoint = 0
    odd_count = 0
    for i in range(node_count - 1, -1, -1):
        if nodes_degrees[i]%2 == 1:
            odd_count += 1
            startpoint = i
  
    if (odd_count > 2):
        print("Number of vertices with odd degrees is greater than 2, there's no eulerian path")
        return
  
    stack = []
    euler_path = []
    current = startpoint
    while (len(stack) > 0) or (sum(adj_matrix[current]) != 0):
        if sum(adj_matrix[current]) == 0:
            euler_path.append(current+1)
            current = stack[-1]
            del stack[-1]
        else:
            for iter in range(node_count):
                if adj_matrix[current][iter] == 1:
                    stack.append(current)
                    adj_matrix[current][iter] = 0
                    adj_matrix[iter][current] = 0
                    current = iter
                    break
    euler_path.append(current+1)

    print(f"eulerian path = {euler_path}")
