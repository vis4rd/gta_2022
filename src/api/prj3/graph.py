import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

from src.api.prj1.generate_random_graph import generate_with_edge_count
from src.api.prj3.edge import *
from src.api.prj3.node import *
from src.api.prj3.functions import node_with_smallest_d, print_node_set


class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.weight = [0 for _e in edges]

    def print_edges_with_weight(self):
        print("Krawedzie wraz z waga:")
        j = 0
        for i in self.edges:
            print("[", i.begin, "-", i.end, "] - waga:", self.weight[j])
            j = j + 1

    def edge_add(self, begin, end):
        if self.edge_exist(begin, end) or begin == end:
            return False
        self.edges.append(Edge(begin, end))
        return True

    def edge_add_with_weight(self, begin, end, weight):
        if self.edge_exist(begin, end) or begin == end:
            return False
        self.edges.append(Edge(begin, end))
        self.weight.append(weight)
        return True

    def edge_find(self, index1, index2):
        for i, edge in enumerate(self.edges):
            if (edge.begin == index1 and edge.end == index2) or (
                edge.begin == index2 and edge.end == index1
            ):
                return edge, i
        return None, -1

    def edge_exist(self, index1, index2):
        temp, index = self.edge_find(index1, index2)
        if index >= 0:
            return True
        else:
            return False

    def edge_delete(self, index1, index2):
        temp, index = self.edge_find(index1, index2)
        if index >= 0:
            del self.edges[index]
            return True
        return False

    def node_add(self, node):
        self.nodes.append(node)

    def node_delete(self, index):
        del self.nodes[index]

    def nodes_add(self, quantity):
        for i in range(quantity):
            self.node_add(Node(i))

    def neighbour_add(self, index, neighbour):
        if (index == neighbour) or (neighbour in self.nodes[index].neighbours):
            return False
        self.nodes[index].neighbours.append(neighbour)
        return True

    def neighbours_add(self, node1, node2):
        temp1 = self.neighbour_add(node1, node2)
        temp2 = self.neighbour_add(node2, node1)
        return temp1 and temp2

    def complete_from_adj_list(self, adj_list):
        rows = len(adj_list)
        self.nodes_add(rows)
        for i in range(rows):
            line = adj_list[i]
            for j in range(len(line)):
                self.neighbour_add(i, int(line[j]) - 1)
                self.edge_add(i, int(line[j]) - 1)

    def delete_everything(self):
        self.nodes = []
        self.edges = []
        self.weight = []

    # zadanie 1
    def is_connected(self):
        max_count = self.largest_component()
        return max_count == len(self.nodes)

    def largest_component(self):
        temp_components = list(self.components())
        temp_components.sort()

        max_count = 0
        # temp_largest = -1
        previous = -1

        for component in temp_components:
            if component != previous:
                previous = component
                count = 0
            count += 1
            if count > max_count:
                max_count = count
                # temp_largest = c
        return max_count

    def components(self):
        temp_component = [-1 for _ in range(len(self.nodes))]
        number = 0

        for i in range(len(self.nodes)):
            if temp_component[i] == -1:
                number += 1
                temp_component[i] = number
                self.components_recursive(number, i, temp_component)
        return temp_component

    def components_recursive(self, number, i, temp_component):
        for j in self.nodes[i].neighbours:
            if temp_component[j] == -1:
                temp_component[j] = number
                self.components_recursive(number, j, temp_component)

    def generate_random_graph(self, nodes_number):
        nodes = nodes_number

        edges = random.randint(nodes - 1, int(nodes * (nodes - 1) / 2))

        self.complete_from_adj_list(generate_with_edge_count(nodes, edges))

    def generate_random_connected_graph(self, nodes_number):
        self.generate_random_graph(nodes_number)
        while not self.is_connected():
            self.delete_everything()
            self.generate_random_graph(nodes_number)

    def add_random_weight(self):
        self.weight = [random.randint(1, 10) for i in range(len(self.edges))]

    def draw_graph_with_weight(self):
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node.number)
        for edge, weight in zip(self.edges, self.weight):
            G.add_edge(edge.begin, edge.end, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, font_weight="bold")
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def draw_di_graph_with_weight(self):
        g = nx.DiGraph()
        for node in self.nodes:
            g.add_node(node.number)
        for edge, weight in zip(self.edges, self.weight):
            g.add_edge(edge.begin, edge.end, weight=weight)
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, arrows=True, font_weight="bold")
        labels = nx.get_edge_attributes(g, "weight")
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.show()

    def dijkstra_algorithm(self, d, p, s, flag=True):
        self.prepare_p_d(d, p, s)
        S = []
        while len(S) != len(self.nodes):
            u = node_with_smallest_d(S, d)
            S.append(u)
            for u_neighbour in self.nodes[u].neighbours:
                if u_neighbour not in S:
                    self.relax(u, u_neighbour, d, p)
        if flag:
            print_node_set(S, d, p)

    def prepare_p_d(self, d, p, s):
        for node in range(len(self.nodes)):
            d.append(float("inf"))
            p.append(None)
        d[s] = 0

    def relax(self, u, u_neighbour, d, p):
        t_edges = [(edge.begin, edge.end) for edge in self.edges]
        try:
            i = t_edges.index((u, u_neighbour))

        except ValueError:
            i = t_edges.index((u_neighbour, u))

        weight = self.weight[i]

        if d[u_neighbour] > (d[u] + weight):
            d[u_neighbour] = d[u] + weight
            p[u_neighbour] = u

    def calculate_distance_matrix(self, distnace_matrix):
        for i in range(len(self.nodes)):
            d = []
            p = []
            self.dijkstra_algorithm(d, p, i, False)
            # distnace_matrix = np.vstack([distnace_matrix, d])
            distnace_matrix[i] = d

    def prim_algorithm(self):
        # tree with one node
        T = [self.nodes[0]]
        # others nodes
        W = self.nodes[1:]

        edges = []
        # while W is not empty
        while W:
            W_numbers = [node.number for node in W]
            edge = [0, 1]
            weight = float("inf")
            for selected_node in T:
                temp = self.find_edge_to_new_nodes(W_numbers, selected_node)
                if temp[0] < weight:
                    weight = temp[0]
                    edge = temp[1]

            if edge[0] in W_numbers:
                number = edge[0]
            else:
                number = edge[1]

            node_to_move = self.find_node_using_number(number)
            T.append(node_to_move)
            W.remove(node_to_move)
            edges.append(edge)

        print("Minimum spanning tree: ", edges)

    def find_edge_to_new_nodes(self, W_numbers, selected_node):
        edge = [0, 1]
        weight = float("inf")

        for i in range(len(self.edges)):
            if (
                (self.edges[i].begin == selected_node.number)
                and (self.edges[i].end in W_numbers)
            ) or (
                (self.edges[i].end == selected_node.number)
                and (self.edges[i].begin in W_numbers)
            ):
                if weight > self.weight[i]:
                    weight = self.weight[i]
                    edge = [self.edges[i].begin, self.edges[i].end]

        return weight, edge

    def find_node_using_number(self, number):
        for node in self.nodes:
            if node.number == number:
                return node

    # Projekt 4

    def components_R2(self, v, visited, stack):
        for u in v.neighbours:
            if u not in visited:
                visited[u] = v
                self.components_R2(self.nodes[u], visited, stack)
        stack.append(v.number)

    def generate_random_digraph(self, min_nodes, max_nodes, p):
        nodes = random.randint(min_nodes, max_nodes)
        self.fill_random_NP_digraph(nodes, p)

    def fill_random_NP_digraph(self, n, p):
        self.nodes_add(n)
        for i in self.nodes:
            for j in self.nodes:
                probability = random.random()
                if probability <= p and i != j:
                    self.edge_add(i.number, j.number)
                    self.neighbour_add(i.number, j.number)

    def to_adjacency_matrix(self):
        nodes_len = len(self.nodes)
        zeros = [[0 for _ in range(nodes_len)] for _ in range(nodes_len)]

        for node in self.nodes:
            for neighbour in node.neighbours:
                zeros[node.number][neighbour] = 1
        return zeros

    def from_adjacency_matrix(self, matrix):
        graph = Graph()
        graph.nodes_add(len(matrix))
        for row_idx in range(len(matrix)):
            row = matrix[row_idx]
            for col_idx in range(len(row)):
                if matrix[row_idx][col_idx] > 0:
                    graph.neighbour_add(row_idx, col_idx)
                    graph.edge_add(row_idx, col_idx)
        return graph

    def transpose(self):
        matrix = self.to_adjacency_matrix()
        rows = len(matrix)
        columns = len(matrix[0])

        matrix_T = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

        G_T = self.from_adjacency_matrix(matrix_T)
        return G_T

    def dfs_visit_digraph(self, v, d, stack, t):
        t += 1
        d[v.number] = t
        for neighbour in v.neighbours:
            if d[neighbour] == -1:
                self.dfs_visit_digraph(self.nodes[neighbour], d, stack, t)
        t += 1
        stack.append(v)

    def kosaraju(self):
        d = {node.number: -1 for node in self.nodes}
        stack = []
        t = 0

        for node in self.nodes:
            if d[node.number] == -1:
                self.dfs_visit_digraph(node, d, stack, t)

        G_T = self.transpose()
        components = []
        visited = {}
        i = 0
        while stack != []:
            v = stack.pop()
            if v.number in visited:
                continue
            else:
                components.append([])
                if v.number not in visited:
                    visited[v.number] = True
                    G_T.components_R2(v, visited, components[i])
                i += 1

        return components

    def bellman_ford(self, src):
        dist = [float("Inf")] * len(self.nodes)
        dist[src] = 0
        p = [0] * len(self.nodes)

        for _ in range(len(self.nodes) - 1):
            for e in self.edges:
                self.relax(e.begin, e.end, dist, p)

        for i, e in enumerate(self.edges):
            if (
                dist[e.begin] != float("Inf")
                and dist[e.begin] + self.weight[i] < dist[e.end]
            ):
                print("Graph contains negative weight cycle")
                return False
        return dist

    def add_S(self):
        G_ = self.create_copy()
        new_node = Node(len(self.nodes))
        G_.node_add(new_node)
        for node in G_.nodes:
            if node.number != new_node.number:
                G_.neighbour_add(new_node.number, node.number)
                G_.edge_add(new_node.number, node.number)
                G_.weight.append(0)

        return G_, new_node

    def create_copy(self):
        copy = Graph()
        copy.nodes = [n for n in self.nodes]
        copy.edges = [e for e in self.edges]
        copy.weight = [w for w in self.weight]
        return copy

    def johnson(self):
        g_, begin = self.add_S()
        bell_dist = g_.bellman_ford(begin.number)
        if not bell_dist:
            return False
        p = [0] * len(self.nodes)
        for node in g_.nodes:
            for neighbour in node.neighbours:
                w = g_.weight[neighbour]
                g_.weight[node.number] = (
                    w + bell_dist[node.number] - bell_dist[neighbour]
                )

        g_.node_delete(begin.number)

        dij_distance = [[] for _ in self.nodes]
        result = {}
        for u in g_.nodes:
            result[u.number] = {}
            g_.dijkstra_algorithm(dij_distance[u.number], p, u.number, False)
            for v in self.nodes:
                result[u.number][v.number] = (
                    dij_distance[u.number][v.number]
                    - bell_dist[u.number]
                    + bell_dist[v.number]
                )

        return result
