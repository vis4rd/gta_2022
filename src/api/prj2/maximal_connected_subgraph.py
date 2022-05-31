import logging as log

def maximal_connected_subgraph(adj_list):
    subgraph_list = all_connected_subgraphs(adj_list)
    max = 0
    index = -1
    for subgraph in range(len(subgraph_list)):
        if max < len(subgraph_list[subgraph]):
            max = len(subgraph_list[subgraph])
            index = subgraph

    return subgraph_list[index]

def all_connected_subgraphs(adj_list):
    size = len(adj_list)
    log.debug(f"size = {size}")

    components = [-1 for _ in range(size)]
    subgraph_list = []

    cc_index = 0  # connected component index
    for node in range(size):
        log.debug(f"Iteration {node}")
        if components[node] == -1:
            cc_index += 1
            components[node] = cc_index
            connected_subgraph(cc_index, node, components, adj_list)
        log.debug(f"components = {components}")
    
    # translation to a list of subgraphs, each subgraph stores nodes' indices
    for subgraph in range(1, cc_index+1):
        subgraph_list.append([el+1 for el in range(size) if components[el] == subgraph])
    
    return subgraph_list


def connected_subgraph(cc_index, node, components, adj_list):
    size = len(adj_list)

    for neighbor in range(1, size+1):
        if neighbor in adj_list[node]:
            log.debug(f"Found neighbor {neighbor} in {adj_list[node]}")
            if components[neighbor-1] == -1:
                log.debug(f"Neighbor == -1")
                components[neighbor-1] = cc_index
                connected_subgraph(cc_index, neighbor-1, components, adj_list)
