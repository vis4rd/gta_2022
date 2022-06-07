import numpy as np


def create_and_draw_connected_graph_with_weight(graph, nodes_number):
    graph.generate_random_connected_graph(nodes_number)
    graph.add_random_weight()
    graph.draw_graph_with_weight()


def create_and_draw_connected_graph_with_weight_dijkstra(graph, nodes_number, s):
    graph.generate_random_connected_graph(nodes_number)
    graph.add_random_weight()

    graph.print_edges_with_weight()

    if s > nodes_number - 1:
        s = nodes_number - 1

    d = []
    p = []

    graph.dijkstra_algorithm(p, d, s)

    # graph.draw_graph_with_weight()


def graph_center(distance_matrix):
    temp = np.sum(distance_matrix, axis=0)
    print(
        "Centrum = ", np.argmin(temp), "(suma odleglosci: ", temp[np.argmin(temp)], ")"
    )


def minimax(distance_matrix):
    temp_minimax = np.amax(distance_matrix, axis=0)

    index_minimax = np.argmin(temp_minimax, axis=0)
    print(
        "Centrum minimax = ",
        index_minimax,
        "(odleglosc od najdalszego: ",
        temp_minimax[index_minimax],
        ")",
    )


def print_node_set(S, d, p):
    print(f"START: S = {S[0]}")

    temp_S = list(S)
    temp_S.sort()
    for i in temp_S:
        print(f"d({i}) = {d[i]} ==> [", end="")
        indx = i
        path = None
        path = [indx]
        prev_indx = p[indx]
        while prev_indx is not None:
            path.append(prev_indx)
            indx = prev_indx
            prev_indx = p[indx]

        for node in reversed(path):
            if node == path[0]:
                print(f" {node} ]")
            else:
                print(f" {node} -", end="")


def node_with_smallest_d(S, d):
    min_distance = float("inf")
    node = None
    for i, temp_distance in enumerate(d):
        if i not in S:
            if min_distance > temp_distance:
                node = i
                min_distance = temp_distance
    return node
