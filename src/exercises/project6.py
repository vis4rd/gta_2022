#!/usr/bin/env python3
import re
import os
from ast import literal_eval


from src.api.prj6.directed_graph import DirectedGraph
from src.api.prj6.directed_graph import SimpleGraph
from src.api.prj6.graph_builder import GraphBuilder as gb
from src.api.prj6.algorithms import (
    page_rank,
    simulated_annealing,
    circuit_length,
    number_to_alpha,
)


def alpha_to_adjacency_list(l):
    print(l)
    l = re.sub(r"\d", "", l)
    l = re.sub(r":(.*)", r":{\g<1>},\n", l)

    print("\n")
    print(l)

    l = re.sub(r"\s", "", l)
    l = f"{{{l}}}"

    print("\n")
    print(l)

    return literal_eval(alpha_to_numbers(l))


def alpha_to_numbers(string):
    alph = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    result = ""
    for c in string:
        if c in alph:
            result += str(alph.index(c) + 1)
        else:
            result += c
    return result


def display_pagerank(rank):
    rank_list = sorted(rank.items(), key=lambda x: x[1], reverse=True)
    for node, score in rank_list:
        print(f"{number_to_alpha(node)} ==> PageRank = {score:.6f}")


with open("src/exercises/input1.txt", "r") as f:
    alpha_list_2 = f.read()


adjacency_list_2 = alpha_to_adjacency_list(alpha_list_2)


def example01a():
    g = DirectedGraph().from_adjacency_list(adjacency_list_2)
    print(g)
    rank = page_rank(g, algorithm="random_walk")
    display_pagerank(rank)


def example01b():
    g = DirectedGraph().from_adjacency_list(adjacency_list_2)
    print(g)
    rank = page_rank(g, algorithm="matrix")
    display_pagerank(rank)


def example02inputdata():
    g = SimpleGraph().from_coordinates("src/exercises/input.dat")
    P = None
    # for MAX_IT in range(10, 150, 5):
    P = simulated_annealing(g, 10000, save=True, P=P)
    length = circuit_length(g.to_adjacency_matrix(), P)
    with open("P_5.tmp", "a") as f:
        f.write(f"{length:.3f}, {P}\n")


def example02random2Dgraph():
    g = gb.get_random_2D_graph(size=50)
    P = None
    for _ in range(100):
        P = simulated_annealing(g, save=True, P=P)
        length = circuit_length(g.to_adjacency_matrix(), P)
        with open("P_6.tmp", "a") as f:
            f.write(f"{length:.3f}, {P}\n")
