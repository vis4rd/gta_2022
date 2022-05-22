
from cmath import inf
from turtle import distance

import networkx as nx
import numpy as np


import random
from api.prj1.generate_random_graph import generate_with_edge_count
from edge import *
from node import *
from functions import node_with_smallest_d, print_node_set

import matplotlib.pyplot as plt

class Graph: 
    def __init__(self, nodes=[],edges=[]):
        self.nodes = [n for n in nodes]
        self.edges = [e for e in edges]
        self.weight = [0 for _e in edges]

    #Edges
    def edge_add (self, begin, end):
        if self.edge_exist(begin, end) or begin == end:
            return False
        self.edges.append(Edge(begin, end))
        return True

    def edge_add_with_weight (self, begin, end, weight):
        if self.edge_exist(begin, end) or begin == end:
            return False
        self.edges.append(Edge(begin, end))
        self.weight.append(weight)
        return True

    def edge_find(self, index1, index2):
        for i, edge in enumerate(self.edges):
            if (edge.begin == index1 and edge.end == index2) or (edge.begin == index2 and edge.end == index1):
                return edge, i 
        return None, -1

    def edge_exist(self, index1, index2):
        temp, index = self.edge_find(index1,index2)
        if index >=0:
            return True 
        else:
            return False

    def edge_delete( self, index1, index2):
        temp, index = self.edge_find(index1,index2)
        if index >=0:
            del self.edges[index]
            return True
        return False


    #Nodes
    def node_add(self, node):
        self.nodes.append(node)

    def node_delete(self, index):
        del self.nodes[index]

    def nodes_add (self, quantity):
        for i in range (quantity):
            self.node_add(Node(i))


    #Neighbours

    def neighbour_add (self, index, neighbour):
        if (index==neighbour) or (neighbour in self.nodes[index].neighbours):
            return False
        self.nodes[index].neighbours.append(neighbour)
        return True


    def neighbours_add (self, node1,node2):
        temp1 = self.neighbour_add(node1,node2)
        temp2 = self.neighbour_add(node2,node1)
        return temp1 and temp2

    #uzpelnianie grafu na podstawie listy 
    def complete_from_adj_list(self, adj_list):
        rows = len (adj_list)
        self.nodes_add(rows)
        for i in range(rows):
            line = adj_list[i]
            for j in range(len(line)):
                self.neighbour_add(i, int(line[j])-1)
                self.edge_add(i, int(line[j])-1)

    #Clean
    def delete_everything(self):
        self.nodes = []
        self.edges = []
        self.weight = []


    #zadanie 1
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
                previous=component
                count=0
            count+=1
            if count > max_count:
                max_count = count
                # temp_largest = c 
        return max_count

    def components(self):
        temp_component = [-1 for _ in range (len(self.nodes))]
        number = 0

        for i in range(len(self.nodes)):
            if temp_component[i] == -1:
                number += 1
                temp_component[i]= number
                self.components_recursive(number, i, temp_component)
        return temp_component

    def components_recursive(self, number, i , temp_component):
        for j in self.nodes[i].neighbours:
            if temp_component[j] == -1:
                temp_component[j] = number
                self.components_recursive(number, j, temp_component)




    def generate_random_graph(self,nodes_number):
        nodes = nodes_number

        edges = random.randint(nodes-1,int (nodes* (nodes - 1)/2 ))

        self.complete_from_adj_list(generate_with_edge_count(nodes,edges))

    def generate_random_connected_graph(self, nodes_number):
        self.generate_random_graph(nodes_number)
        while not self.is_connected():
            self.delete_everything()
            self.generate_random_graph(nodes_number)

    def add_random_weight(self):
        self.weight= [random.randint(1,10) for i in range(len(self.edges))]

    def draw_graph_with_weight(self):
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node.number)
        for edge, weight in zip(self.edges, self.weight):
            G.add_edge(edge.begin, edge.end, weight=weight)
        pos=nx.spring_layout(G)
        nx.draw_networkx(G,pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    #zadanie 2

    def dijkstra_algorithm(self,d,p,s, flag = True):
        self.prepare_p_d(d,p,s)

        S = []
        while len(S) != len(self.nodes):
            u = node_with_smallest_d(S,d)
            S.append(u)
            for u_neighbour in self.nodes[u].neighbours:
                if u_neighbour not in S:
                    self.relax(u,u_neighbour,d,p)
        if flag:
            print_node_set(S,d,p)

    def prepare_p_d(self,d,p,s):
        for node in range(len(self.nodes)):
            d.append(float('inf'))
            p.append(None)
        d[s] = 0

    def relax(self, u, u_neighbour,d,p):

        t_edges = [(edge.begin, edge.end)for edge in self.edges ]
        try: 
            i = t_edges.index((u,u_neighbour))
        
        except ValueError:
            i = t_edges.index((u_neighbour,u))

        weight = self.weight[i]

        if d[u_neighbour] > (d[u] + weight):
            d[u_neighbour] = (d[u] + weight)
            p[u_neighbour] = u  

    #zadanie 3
    def calculate_distance_matrix(self, distnace_matrix):
        for i in range(len(self.nodes)):
            d = []
            p = []
            self.dijkstra_algorithm(p, d, i,False)
            print(d)
            distnace_matrix = np.vstack([distnace_matrix, d])

  
