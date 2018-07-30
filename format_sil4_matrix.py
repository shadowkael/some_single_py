__author__ = 'Chanlone'

ROOT_DIR = 'E:\\sil4_test\\result\\trace-3.14.63\\system_calls\\'
TARGET_DIR = 'E:\\sil4_test\\result\\net_3_14_63\\'

import os

SYSTEM_CALL_LIST = os.listdir(ROOT_DIR)
os.chdir(ROOT_DIR)
NEST_SPACE = 2
INIT_VALUE = 0


def walk_system_call_list():
    for system_call in SYSTEM_CALL_LIST:
        process_dir = ROOT_DIR + system_call + "\\sys_tree"
        if os.path.isdir(process_dir):
            os.chdir(process_dir)
        else:
            continue
        log_line = dict()
        vertices = list()
        for log_and_sys_tree in sorted(os.listdir(os.getcwd())):
            if not os.path.isfile(os.getcwd() + "\\" + log_and_sys_tree):
                continue
            # count every weight of sys_tree and store in log_line
            if log_and_sys_tree.endswith("log"):
                log_line[log_and_sys_tree.split('_')[0]] = get_line_num(log_and_sys_tree)
            # write contact of vertices
            elif log_and_sys_tree.startswith('sys'):
                vertices.extend(generate_vertices(log_and_sys_tree))
        # generate vertices and write in file
        vertices_unique = list(set(vertices))
        vertices_unique.sort(key=vertices.index)

        # write file head and point info
        target_file_name = 'Matrix_' + system_call + '.net'
        write_file_head(target_file_name, len(vertices_unique))
        write_file_point(target_file_name, vertices_unique)

        # init matrix with '0'
        init_matrix = generate_init_matrix(len(vertices_unique))
        result_matrix = list()
        result_matrix.extend(init_matrix)
        for log_and_sys_tree in sorted(os.listdir(os.getcwd())):
            if not os.path.isfile(os.getcwd() + "\\" + log_and_sys_tree):
                continue
            if log_and_sys_tree.startswith('sys'):
                sys_tree_num = log_and_sys_tree.split('_')[-1]
                data_format_matrix(log_and_sys_tree, log_line[sys_tree_num], vertices_unique,
                                   result_matrix)
        write_file_matrix(target_file_name, init_matrix)


def generate_init_matrix(matrix_num):
    init_matrix = list()
    for i in range(matrix_num):
        init_row = list()
        for k in range(matrix_num):
            init_row.append(INIT_VALUE)
        init_matrix.append(init_row)
    return init_matrix


def data_format_matrix(format_file, sys_tree_weight, source_list, matrix):
    with open(format_file, 'r') as sil4_data:
        data_copy = sil4_data.readlines()
        for index, data_out_line in enumerate(data_copy):
            # Count space in each line
            space_out_num = get_space_num(data_out_line)
            # judge each line nest
            data_inner = data_copy[index + 1:]
            for inner_index, data_inner_line in enumerate(data_inner):
                space_inner_num = get_space_num(data_inner_line)
                if space_out_num == space_inner_num - NEST_SPACE:
                    row_index = source_list.index(data_out_line.strip())
                    cow_index = source_list.index(data_inner_line.strip())
                    matrix[row_index][cow_index] = matrix[row_index][cow_index] + sys_tree_weight
                    # output_function(index, inner_index + 1)
                elif space_out_num >= space_inner_num:
                    break
    return matrix


def generate_vertices(sys_tree_file):
    with open(sys_tree_file, 'r') as sil4_data:
        vertices_list = sil4_data.readlines()
        for index, vertices in enumerate(vertices_list):
            vertices_list[index] = vertices.strip()
    return vertices_list


def get_space_num(data_str):
    return len(data_str) - len(data_str.strip(' '))


def get_line_num(log_file):
    with open(log_file, 'r') as line_num:
        return sum(line.count("\n") for line in block(line_num))


def block(log_file, size=65536):
    while True:
        nb = log_file.read(size)
        if not nb:
            break
        yield nb


def write_file_head(graph_file, point_num):
    if TARGET_DIR:
        graph_file = TARGET_DIR + graph_file
    with open(graph_file, 'w') as file_head:
        head_str = "*Vertices\t" + str(point_num) + "\n"
        file_head.write(head_str)


def write_file_point(graph_file, points):
    if TARGET_DIR:
        graph_file = TARGET_DIR + graph_file
    with open(graph_file, 'a') as file_points:
        for index, point in enumerate(points):
            points_str = "\t" + str(index + 1) + " " + '"' + point.strip() + '"' + "\n"
            file_points.write(points_str)


def write_file_arcs(graph_file, arcs):
    if TARGET_DIR:
        graph_file = TARGET_DIR + graph_file
    with open(graph_file, 'a') as file_arcs:
        file_arcs.write("*Arcs\n")
        for i in arcs:
            file_arcs.write(i)


def write_file_matrix(graph_file, matrix):
    if TARGET_DIR:
        graph_file = TARGET_DIR + graph_file
    with open(graph_file, 'a') as file_matrix:
        file_matrix.write("*Matrix\n")
        for i in matrix:
            file_matrix.write("\t")
            for k in i:
                file_matrix.write(str(k) + " ")
            file_matrix.write("\n")


if __name__ == "__main__":
    walk_system_call_list()
