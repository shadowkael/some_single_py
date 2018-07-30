__author__ = 'Chanlone'

import os

ROOT_DIR = "E:\\sil4_test"
VERTICES_FILE = "vertices.rs"
ARCS_FILE = "arcs.rs"
TARGET_FILE = 'new_kernel_net.net'
os.chdir(ROOT_DIR)


# return a list only store vertices in every item.
def format_vertices_data(vertices_file):
    data_vertices = list()
    with open(vertices_file, 'r') as vertices_read:
        data_copy = vertices_read.readlines()
        for data in data_copy:
            data_vertices.append(data.split('"')[1])
    return data_vertices


def test_arcs(test_file):
    test_arcs_list = list()
    with open(test_file, 'r') as test_arcs_file:
        test_arcs_list = test_arcs_file.readlines()
        for index, arcs_temp in enumerate(test_arcs_list):
            test_arcs_list[index] = eval(arcs_temp)
    return test_arcs_list


# return a list cut repeat space
def arcs_cut_repeat_space(arcs_file):
    data_arcs = list()
    with open(arcs_file, 'r') as arcs_read:
        data_copy = arcs_read.readlines()
        for arc in data_copy:
            data_arcs.append(arc.split())
    return data_arcs


# return a list transform id to kernel's function name
def id_to_name(vertices_list, arcs_list):
    for index, arc in enumerate(arcs_list):
        arcs_list[index][0] = vertices_list[int(arc[0]) - 1]
        arcs_list[index][1] = vertices_list[int(arc[1]) - 1]
    return arcs_list


# return a list just like a set, every item is unique
def get_unique_list(old_list):
    new_list = list(set(old_list))
    new_list.sort(key=old_list.index)
    return new_list


def name_to_id(vertices_list, arcs_list):
    for index, arc in enumerate(arcs_list):
        arcs_list[index][0] = vertices_list.index(arc[0]) + 1
        arcs_list[index][1] = vertices_list.index(arc[1]) + 1
        arcs_list[index][2] = int(arcs_list[index][2])
    return arcs_list


# input list source,data format:[[1,2,100],[2,103,57],...,[5,6,118000]]
def arcs_cut_repeat(arcs_list):
    new_arcs_list = list()
    pop_list = list()

    for index_out, arc_out in enumerate(arcs_list):
        arc_item = list()
        arc_item.extend(arc_out)
        for index_inner, arc_inner in enumerate(arcs_list[index_out + 1:]):
            if (index_inner + 1 + index_out) in pop_list:
                continue
            if arc_out[0] == arc_inner[0] and arc_out[1] == arc_inner[1]:
                arc_item[2] = int(arc_item[2] + arc_inner[2])
                pop_list.append(index_inner + index_out + 1)
        if index_out not in pop_list:
            new_arcs_list.append(arc_item)
    return new_arcs_list


def write_file_point(graph_file, points):
    with open(graph_file, 'w') as file_points:
        for index, point in enumerate(points):
            points_str = "\t" + str(index + 1) + " " + '"' + point.strip() + '"' + "\n"
            file_points.write(points_str)


def write_file_arcs(arcs_file, arcs_data):
    with open(arcs_file, 'w') as arcs_files:
        # arcs_files.write("*Arcs\n")
        for i in arcs_data:
            arcs_files.write(str(i) + "\n")


if __name__ == "__main__":
    vertices = format_vertices_data(VERTICES_FILE)
    arcs = arcs_cut_repeat_space(ARCS_FILE)

    name_arcs = id_to_name(vertices, arcs)
    unique_vertices = get_unique_list(vertices)
    write_file_point("E:\\sil4_test\\test_unique_vertices", unique_vertices)
    id_arcs = name_to_id(unique_vertices, name_arcs)

    unique_arcs = arcs_cut_repeat(test_arcs("E:\\sil4_test\\temp_arcs"))
    write_file_arcs("E:\\sil4_test\\test_arcs", unique_arcs)
    #
    # print unique_arcs.__len__()
