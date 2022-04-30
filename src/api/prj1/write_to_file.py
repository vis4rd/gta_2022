def _write_matrix_to_file(filename, list):
    with open(filename, 'w') as file:
        for row in list:
            for element in row:
                file.write(str(element)+" ")
            file.write("\n")

def write_incidence_matrix_to_file(matrix):
    _write_matrix_to_file("Mi.txt", matrix)

def write_adjacency_matrix_to_file(matrix):
    _write_matrix_to_file("Ms.txt", matrix)

def write_adjacency_list_to_file(list):
    _write_matrix_to_file("Ls.txt", list)

def write_all_formats(adj_matrix, adj_list, incidence_matrix):
    write_incidence_matrix_to_file(incidence_matrix)
    write_adjacency_matrix_to_file(adj_matrix)
    write_adjacency_list_to_file(adj_list)
