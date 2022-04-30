# from xmlrpc.client import boolean
import logging as log

from .MiMs import MiMs
from .MsLs import MsLs
from .LsMs import LsMs
from .MsMi import MsMi
from .draw_graph import DrawGraph
from .write_to_file import *

def _assume_incidence_matrix(inc_matrix): # IM
    log.info("Input assumed as incidence matrix")
    adj_matrix = MiMs(inc_matrix)
    adj_list = MsLs(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    DrawGraph(adj_list)

def _assume_adjacency_list(adj_list): # AL
    log.info("Input assumed as adjacency list")
    adj_matrix = LsMs(adj_list)
    inc_matrix = MsMi(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    DrawGraph(adj_list)

def _assume_adjacency_matrix(adj_matrix): # AM
    log.info("Input assumed as adjacency matrix")
    adj_list = MsLs(adj_matrix)
    inc_matrix = MsMi(adj_matrix)
    write_all_formats(adj_matrix, adj_list, inc_matrix)
    DrawGraph(adj_list)

def parse_input(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])

    for row in matrix: # check the element count in the row
        if column_count != len(row): # if not rectangular matrix
            _assume_adjacency_list(matrix)
            return

    if row_count == column_count: # if the matrix is rectangular
        _assume_adjacency_matrix(matrix)
    else:
        _assume_incidence_matrix(matrix)
