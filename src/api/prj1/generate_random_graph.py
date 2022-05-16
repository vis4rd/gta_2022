import random

def _generate_all_possible_connections(node_count):
    list = []
    for first in range(1, node_count+1):
        for second in range(first+1, node_count+1):
            list.append([first, second])
    return list

# Returns adjacency list
def generate_with_edge_count(node_count, edge_count):
    max_edge_count = int((node_count-1) * node_count / 2)
    if edge_count > max_edge_count:
        edge_count = max_edge_count
    options = _generate_all_possible_connections(node_count)

    random.shuffle(options)
    random.shuffle(options)
    edges = options[0:edge_count]

    adjacency_list = [[] for i in range(node_count)]
    for node, neighbor in edges:
        adjacency_list[node-1].append(neighbor)
        adjacency_list[neighbor-1].append(node)

    return adjacency_list

# Returns adjacency list
def generate_with_probability(node_count, probability):
    if probability < 0.0:
        return [[] for i in range(node_count)]
    if probability > 1.0:
        probability = 1.0
    
    options = _generate_all_possible_connections(node_count)
    adjacency_list = [[] for i in range(node_count)]
    for node, neighbor in options:
        if random.random() <= probability:
            adjacency_list[node-1].append(neighbor)
            adjacency_list[neighbor-1].append(node)

    return adjacency_list
