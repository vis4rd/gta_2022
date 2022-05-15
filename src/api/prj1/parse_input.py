import logging as log

from .conversions import *
from .write_to_file import *


def _assume_incidence_matrix(inc_matrix): # IM
    log.info("Input assumed as incidence matrix")
    adj_matrix = convert_inc_matrix_to_adj_matrix(inc_matrix)
    adj_list = convert_adj_matrix_to_adj_list(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    return adj_list


def _assume_adjacency_list(adj_list): # AL
    log.info("Input assumed as adjacency list")
    adj_matrix = convert_adj_list_to_adj_matrix(adj_list)
    inc_matrix = convert_adj_matrix_to_inc_matrix(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    return adj_list


def _assume_adjacency_matrix(adj_matrix): # AM
    log.info("Input assumed as adjacency matrix")
    adj_list = convert_adj_matrix_to_adj_list(adj_matrix)
    inc_matrix = convert_adj_matrix_to_inc_matrix(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    return adj_list


def parse_input(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])

    for row in matrix: # check the element count in the row
        if column_count != len(row): # if not rectangular matrix
            return _assume_adjacency_list(matrix)

    if row_count == column_count: # if the matrix is rectangular
        return _assume_adjacency_matrix(matrix)
    else:
        return _assume_incidence_matrix(matrix)
