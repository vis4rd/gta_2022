def convert_adj_matrix_to_inc_matrix(matrix):
    root = 0
    i = 0
    for row in matrix:
        for el in row[i+1:]:
            if el == 1:
                root += 1
        i += 1
    cols, rows = (root, len(matrix))
    inc_matrix = [[0 for i in range(cols)] for j in range(rows)]
    i = 0
    r = 0
    for row in matrix:
        j = i + 1
        for el in row[j:]:
            if el == 1:
                inc_matrix[j][r] = 1
                inc_matrix[i][r] = 1
                r += 1
            j += 1
        i += 1
    return inc_matrix


def convert_adj_matrix_to_adj_list(matrix):
    size = len(matrix)
    adj_list = []
    for row in range(size):
        adj_row_list = []
        for column in range(size):
            if matrix[row][column] == 1: # if element is 1, add its index as neighbor to adjacency list
                adj_row_list.append(column + 1)
        adj_list.append(adj_row_list)
    return adj_list


def convert_inc_matrix_to_adj_matrix(matrix):
    rows, cols = (len(matrix), len(matrix))
    adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
    first = -1
    for column in range(len(matrix[0])):
        for row in range(rows):
            if matrix[row][column] == 1:
                if first >= 0:
                    adj_matrix[first][row] = 1
                    first = -1
                else:
                    first = row
    for row in range(rows):
        diag = row + 1
        for column in range(diag, cols):
            adj_matrix[column][row] = adj_matrix[row][column]
    return adj_matrix


# We assume that the order of rows in the adjacency list corresponds to the order of nodes
#   in the graph (the first row in the list contains neighbors of the first node).
#
# The size of matrix is taken from the length of the adjacency list.
def convert_adj_list_to_adj_matrix(list):
    rows, cols = (len(list), len(list))
    adj_matrix = [[0 for i in range(cols)] for j in range(rows)]
    j = 0
    for row in list: 
        for neighbor_index in row: # obtain subsequent neighbor indices from the list
            adj_matrix[j][neighbor_index-1] = 1
        j += 1

    return adj_matrix


def convert_adj_list_to_inc_matrix(list):
    adj_matrix = convert_adj_list_to_adj_matrix(list)
    return convert_adj_matrix_to_inc_matrix(adj_matrix)
