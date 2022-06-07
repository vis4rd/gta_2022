
import math
import random
import numpy as np
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt

from src.api.prj6.directed_graph import DirectedGraph
from src.api.prj6.directed_graph import SimpleGraph

def page_rank(g: DirectedGraph, d=0.15, algorithm="matrix") -> Dict[int, float]:
    """
    Zwraca ranking węzłów w grafie skierowanym
    d - prawdopodobieństwo teleportacji
    """
    if d < 0 or d > 1:
        raise ValueError("Nieprawidłowa wartość dla prawdopodobieństwa")

    if g.has_dangling_nodes():
        raise ValueError(
            "Nieprawidłowy graf: posiada wierzchołki bez krawędzi wyjściowych."
        )

    if algorithm == "random_walk":
        return _page_rank_random_walk(g, d=d)
    elif algorithm == "matrix":
        return _page_rank_matrix(g, d=d)
    else:
        raise ValueError("Nieprawidłowy wybór algorytmu.")


def _page_rank_random_walk(g: DirectedGraph, d) -> Dict[int, float]:
    adj_l = g.to_adjacency_list()
    visited = {n: 0 for n in g.nodes}
    current_node = random.choice(list(g.nodes))
    N = 0
    while N < 100000:
        if random.random() > d: #and len(adj_l[current_node]) != 0: -----------usuniete na zajeciach
            current_node = random.choice(list(adj_l[current_node]))
        else:
            current_node = random.choice(list(g.nodes))

        visited[current_node] += 1
        N += 1
    return {n: v / sum(visited.values()) for n, v in visited.items()}


def _page_rank_matrix(g: DirectedGraph, d) -> Dict[int, float]:
    n = len(g.nodes)
    P = np.zeros((n, n))
    A = np.array(g.to_adjacency_matrix())
    for i in range(n):
        for j in range(n):
            P[i][j] = (1.0 - d) * A[i][j] / g.node_degree(i + 1) + d / float(n)

    p0 = np.full(n, 1 / n)
    p1 = np.zeros(n)
    i = 0
    err = float("inf")
    while err > 1e-11:
        p1 = p0.dot(P)
        diff = p1 - p0
        err = sum(x ** 2 for x in diff)
        p0 = p1
        i += 1

    print(f"Zbieżność uzyskano po {i} iteracjach.")
    return {k: p1[k - 1] for k in range(1, n + 1)}


def simulated_annealing(g: SimpleGraph, MAX_IT=None, P: List[int] = None, save=False):
    if not g.is_complete():
        return ValueError("Do tego algorytmu graf musi być pełny.")

    if P is None:
        P = [n for n in range(1, len(g) + 1)]
        random.shuffle(P)

    if MAX_IT is None:
        MAX_IT = len(g)

    adj_m = g.to_adjacency_matrix()
    d = circuit_length(adj_m, P)
    for i in range(100, 0, -1):
        T = 0.001 * i ** 2
        for _ in range(MAX_IT):
            # switch: a-b c-d --> a-c b-d
            _, b, c, _ = _choose_nodes(P)
            P[b], P[c] = P[c], P[b]

            d_new = circuit_length(adj_m, P)
            if d_new < d:
                d = d_new
            else:
                r = random.random()
                if r < math.exp(-(d_new - d) / T):
                    d = d_new
                else:
                    # switch back
                    P[b], P[c] = P[c], P[b]

    if save:
        x = [g.x[n - 1] for n in P]
        y = [g.y[n - 1] for n in P]

        # connect first and last point
        x.append(g.x[P[0] - 1])
        y.append(g.y[P[0] - 1])

        plt.plot(x, y, "-o")
        plt.title(f"MAX_IT={MAX_IT}, d={d:.3f}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig("SA.png")
        plt.clf()

    return P


def _choose_nodes(P: List[int]) -> Tuple[int, int, int, int]:
    while True:
        a = random.randrange(len(P))
        b = (a - 1) % len(P) if random.getrandbits(1) else (a + 1) % len(P)
        c = random.randrange(len(P))
        d = (c - 1) % len(P) if random.getrandbits(1) else (c + 1) % len(P)
        nodes = [P[a], P[b], P[c], P[d]]
        if len(set(nodes)) == len(nodes):
            return a, b, c, d


def circuit_length(adj_m, P: List[int]) -> float:
    length = 0.0
    for i in range(len(P)):
        length += adj_m[P[i] - 1][P[(i + 1) % len(P)] - 1]
    return length


def number_to_alpha(num: int) -> str:
    if num < 1:
        raise ValueError()
    if num > 26:
        return number_to_alpha(num // 26) + chr(num % 26 + ord("A") - 1)
    return chr(num + ord("A") - 1)