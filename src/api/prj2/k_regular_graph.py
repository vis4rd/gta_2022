import logging as log

from src.api.prj2.graphic_sequence import generate_with_graphic_sequence

def generate_k_regular_graph(node_count, k):
    if (node_count*k)%2 != 0:
        return [] * node_count

    if k < 0:
        k = 0

    if k >= node_count:
        k = node_count - 1;

    graphic_sequence = [k] * node_count
    adj_list = generate_with_graphic_sequence(graphic_sequence)
    log.debug(f"Graphic sequence = {graphic_sequence}")
    return adj_list
