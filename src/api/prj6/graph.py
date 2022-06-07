from __future__ import annotations

from typing import Set
from abc import ABC, abstractmethod

from src.api.prj6.helper_structures import Node, Edge, Weight


from src.api.prj6.helper_structures import (
    AdjacencyList,
    AdjacencyMatrix,
    IncidenceMatrix,
)






class Graph(ABC):
    def __init__(self, size: int = 0) -> None:
        self.nodes: Set[Node] = set()
        self.edges: Set[Edge] = set()
        self.separator = ""
        self.name = ""

        self.clear()
        self.add_nodes(count=size)

    def add_nodes(self, count: int = 1) -> None:
        """Tworzy nowe wierzchołki"""
        for i in range(len(self) + 1, len(self) + 1 + count):
            self.nodes.add(i)

    def __len__(self) -> int:
        return len(self.nodes)

    def __str__(self) -> str:
        s = ""
        for k, v in sorted(self.to_adjacency_list().items()):
            s += f"{k}: {v}\n"
        return s

    def clear(self) -> None:
        self.nodes.clear()
        self.edges.clear()

    def is_weighted_graph(self) -> bool:
        return any(edge.weight != 1 for edge in self.edges)

    @abstractmethod
    def get_all_possible_edges(self) -> Set[Edge]:
        """
        Returns edges that are all possible moves from edge.begin to edge.end
        Especially usable in simple graphs
        """

    def node_neighbours(self, node: Node) -> Set[Node]:
        """Returns nodes adjacent to a given node"""
        return set([edge.end for edge in self.node_edges(node)])

    def node_edges(self, node: Node) -> Set[Edge]:
        """Returns set of edges adjacent to the given node"""
        return set(
            [edge for edge in self.get_all_possible_edges() if edge.begin == node]
        )

    def node_degree(self, node: Node) -> int:
        """Returns degree of the selected node"""
        return len(self.node_edges(node))

    def edge_to_node(self, begin: Node, end: Node) -> Edge:
        """Get edge that connects given two nodes"""
        edge = [
            e
            for e in self.get_all_possible_edges()
            if e.begin == begin and e.end == end
        ][0]
        return edge

    @abstractmethod
    def connect(self, node1: Node, node2: Node, weight: Weight = 1) -> None:
        """Tworzy krawędż między wierzchołkiem node1 a node2"""

    @abstractmethod
    def disconnect(self, node1: Node, node2: Node) -> None:
        """Usuwa krawędż między wierzchołkiem node1 a node2"""

    @abstractmethod
    def is_connected(self, node1: Node, node2: Node) -> bool:
        """Czy stnieje krawędź node1 -- node2"""

    def to_adjacency_list(self) -> AdjacencyList:
        """Zwraca graf w postaci listy sąsiedztwa"""
        adj_l = {
            (node): (
                set(
                    [
                        edge.end
                        for edge in self.get_all_possible_edges()
                        if edge.begin == node
                    ]
                )
            )
            for node in self.nodes
        }
        return adj_l

    @abstractmethod
    def to_adjacency_matrix(self) -> AdjacencyMatrix:
        """Zwraca graf w postaci macierzy sąsiedztwa"""

    @abstractmethod
    def to_incidence_matrix(self) -> IncidenceMatrix:
        """Zwraca graf w postaci macierzy incydencji"""

    def from_adjacency_list(self, adjacency_list: AdjacencyList) -> Graph:
        """Wypełnianie grafu z listy sąsiedztwa"""
        self.clear()

        size = len(adjacency_list)
        self.add_nodes(size)

        for node, neighbours in adjacency_list.items():
            for neighbour in neighbours:
                self.connect(node, neighbour)
        return self

    