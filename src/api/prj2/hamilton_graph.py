import logging as log

from src.api.prj1.generate_random_graph import generate_with_probability
from src.api.prj1.conversions import convert_adj_list_to_adj_matrix


def _is_safe(adj_matrix, current_node, path_pos, path) -> bool:
    if adj_matrix[path[path_pos-1]-1][current_node] == 0:
        return False

    for node in path:
        if node-1 == current_node:
            return False

    return True


def _hamilton_search(adj_matrix, path, path_pos, node_count) -> bool:
    if path_pos == node_count:
        if adj_matrix[path[path_pos-1]-1][path[0]] == 1:
            return True
        else:
            return False

    for node in range(1, node_count):
        if _is_safe(adj_matrix, node, path_pos, path) == True:
            path[path_pos] = node+1

            if _hamilton_search(adj_matrix, path, path_pos+1, node_count) == True:
                return True
            path[path_pos] = 0

    return False


def find_hamilton_cycle(adj_list):
    node_count = len(adj_list)
    path = [0] * node_count

    adj_matrix = convert_adj_list_to_adj_matrix(adj_list)

    path[0] = 1 # start on the first node in the path
    if _hamilton_search(adj_matrix, path, 1, node_count) == False:
        print ("Solution does not exist\n")
        return

    path.append(path[0])
    return path