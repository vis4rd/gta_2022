import random
import logging as log

from src.api.prj1.draw_graph import draw_graph
from src.api.prj1.generate_random_graph import generate_with_probability
from src.api.prj2.graphic_sequence import generate_with_graphic_sequence

def generate_euler_graph(node_count):
    if node_count < 3:
        log.info(f"node_count({node_count}) < 3, setting it to 3")
        node_count = 3

    graph_adj_list = [[] for _ in range(node_count)]
    even_nodes = []
    while (_is_eulerian(even_nodes, len(graph_adj_list)) is not True) and (_get_edge_count(graph_adj_list) < 1):
        # graphic_sequence = [random.randint(1, int(node_count / 2)) * 2 for _ in range(node_count)]
        # graph_adj_list = generate_with_graphic_sequence(graphic_sequence)
        graph_adj_list = generate_with_probability(node_count, 0.5)
        even_nodes = _get_even_degree_nodes(graph_adj_list)

    log.debug(f"graph_adj_list = {graph_adj_list}")
    graph_copy = graph_adj_list.copy()
    # for node in range(len(graph_adj_list)):
    #     graph_copy[node] = graph_adj_list[node]
    log.debug(f"graph_copy = {graph_copy}")
    euler_cycle = [[] for _ in range(len(graph_copy))]

    draw_graph(graph_copy)
    
    neighbor = 1
    while _get_edge_count(graph_copy) > 0:
        node = neighbor
        try:
            log.debug(f"node = {node}")
            log.debug(f"graph_copy[node-1] = {graph_copy[node-1]}")
        except Exception:
            log.exception(f"node = {node}")
            break
        for neighbor in graph_copy[node-1]:
            graph_copy[node-1].remove(neighbor)
            try:
                log.debug(f"neighbor = {neighbor}")
                log.debug(f"graph_copy[neighbor-1] = {graph_copy[neighbor-1]}")
                graph_copy[neighbor-1].remove(node)
            except Exception:
                log.exception(f"neighbor = {neighbor}")
                break

            if _is_bridge(graph_copy):
                graph_copy[node-1].append(neighbor)
                graph_copy[neighbor-1].append(node)
            else:
                break

        if _is_bridge(graph_copy):
            if neighbor in graph_copy[node-1]:
                graph_copy[node-1].remove(neighbor)
            if node in graph_copy[neighbor-1]:
                graph_copy[neighbor-1].remove(node)
            graph_copy.pop(node-1)
        euler_cycle[node-1].append(neighbor)

    log.debug(f"euler_cycle = {euler_cycle}")
    return euler_cycle

def _is_eulerian(even_nodes, graph_len) -> bool:
    log.debug(f"is_eulerian = {((graph_len - len(even_nodes)) == 0)}")
    return ((graph_len - len(even_nodes)) == 0)

def _get_even_degree_nodes(adj_list):
    even_nodes_list = []
    for node in range(len(adj_list)):
        if len(adj_list[node]) % 2 == 0:
            even_nodes_list.append(node+1)
    log.debug(f"even nodes: {even_nodes_list}")
    return even_nodes_list

def _get_edge_count(adj_list):
    edge_count = 0
    for node in range(1, len(adj_list)+1):
        for _ in adj_list[node-1]:
            edge_count += 1
    log.debug(f"edge_count = {edge_count}")
    return edge_count

def _is_bridge(adj_list) -> bool:
    start = 1
    visited = {}

    for node in range(1, len(adj_list)+1):
        visited[node] = -1
    
    log.debug(f"visited = {visited}")
    visited[start] = 0
    S = [start]
    while len(S) != 0:
        print("shit")
        node = S.pop()
        for neighbor in adj_list[node-1]:
            if (neighbor in visited) and (visited[neighbor] == -1):
                visited[neighbor] = 0
                S.append(neighbor)
            visited[node] = 1
    return list(visited.values()).count(1) != len(adj_list)
