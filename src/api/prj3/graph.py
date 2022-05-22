from cmath import inf
from turtle import distance

import networkx as nx
import numpy as np
<<<<<<< HEAD
=======


import random
from api.prj1.generate_random_graph import generate_with_edge_count
from edge import *
from node import *
from functions import node_with_smallest_d, print_node_set

>>>>>>> 1e696cf (3.3 completed)
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

<<<<<<< HEAD
=======
    def generate_random_graph(self,nodes_number):
        nodes = nodes_number

        edges = random.randint(nodes-1,int (nodes* (nodes - 1)/2 ))

        self.complete_from_adj_list(generate_with_edge_count(nodes,edges))

>>>>>>> 1e696cf (3.3 completed)
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

<<<<<<< HEAD
    def dijkstra_algorithm(self, d, p, s, flag=True):
        self.prepare_p_d(d, p, s)
=======
    #zadanie 2

    def dijkstra_algorithm(self,d,p,s, flag = True):
        self.prepare_p_d(d,p,s)
>>>>>>> 1e696cf (3.3 completed)

        S = []
        while len(S) != len(self.nodes):
            u = node_with_smallest_d(S, d)
            S.append(u)
            for u_neighbour in self.nodes[u].neighbours:
                if u_neighbour not in S:
<<<<<<< HEAD
                    self.relax(u, u_neighbour, d, p)
        if flag:
            print_node_set(S, d, p)
=======
                    self.relax(u,u_neighbour,d,p)
        if flag:
            print_node_set(S,d,p)
>>>>>>> 1e696cf (3.3 completed)

    def prepare_p_d(self, d, p, s):
        for node in range(len(self.nodes)):
            d.append(float("inf"))
            p.append(None)
        d[s] = 0

<<<<<<< HEAD
    def relax(self, u, u_neighbour, d, p):
        t_edges = [(edge.begin, edge.end) for edge in self.edges]
        try:
            i = t_edges.index((u, u_neighbour))

        except ValueError:
            i = t_edges.index((u_neighbour, u))
=======
    def relax(self, u, u_neighbour,d,p):

        t_edges = [(edge.begin, edge.end)for edge in self.edges ]
        try: 
            i = t_edges.index((u,u_neighbour))
        
        except ValueError:
            i = t_edges.index((u_neighbour,u))
>>>>>>> 1e696cf (3.3 completed)

        weight = self.weight[i]

        if d[u_neighbour] > (d[u] + weight):
<<<<<<< HEAD
            d[u_neighbour] = d[u] + weight
            p[u_neighbour] = u

=======
            d[u_neighbour] = (d[u] + weight)
            p[u_neighbour] = u  

    #zadanie 3
>>>>>>> 1e696cf (3.3 completed)
    def calculate_distance_matrix(self, distnace_matrix):
        for i in range(len(self.nodes)):
            d = []
            p = []
<<<<<<< HEAD
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
=======
            self.dijkstra_algorithm(p, d, i,False)
            print(d)
            distnace_matrix = np.vstack([distnace_matrix, d])

  
>>>>>>> 1e696cf (3.3 completed)
