__author__ = 'Chanlone'

# This script can cut repeat info from .net file which is generate by Pajek
# You need separate vertices info and Arcs info into two files, they will be input file
# output also two files, you need add them manually in a new .net file

import os
from cut_repeat import format_vertices_data, arcs_cut_repeat_space, id_to_name, get_unique_list, write_file_point, \
    write_file_arcs

ROOT_DIR = "E:\\sil4_test"
VERTICES_FILE = "vertices.rs"
ARCS_FILE = "arcs.rs"
os.chdir(ROOT_DIR)


def get_arcs_dict(name_arcs):
    arcs_dict = dict()
    for index, value in enumerate(name_arcs):
        key = name_arcs[index][0] + '%' + name_arcs[index][1]
        if key in arcs_dict:
            arcs_dict[key] = int(arcs_dict[key]) + int(name_arcs[index][2])
        else:
            arcs_dict[key] = name_arcs[index][2]
    return arcs_dict


def name_to_id(arcs_dict, vertices_list):
    arcs_list = list()
    for key in arcs_dict:
        key_0 = key.split('%')
        arcs_list.append(
            '\t' + str(get_id(key_0[0], vertices_list)) + ' ' + str(get_id(key_0[1], vertices_list)) + ' ' + str(
                arcs_dict[key]))
    return arcs_list


def get_id(vertices_name, vertices_list):
    init_id = vertices_list.index(vertices_name) + 1
    return init_id


if __name__ == "__main__":
    # From vertices file read data and format it into a list
    vertices = format_vertices_data(VERTICES_FILE)
    # From arcs file read data and format it into a list
    # format like [['1','2','100'],['2','4','90'],...,['24','7','10']]
    arcs = arcs_cut_repeat_space(ARCS_FILE)

    # Transform the vertices id in arcs list to vertices name
    name_arcs = id_to_name(vertices, arcs)
    # Just like K-V mapping, loop every item in name_arcs
    # item[0] and item[1] as a key, item[2] as a value and store in a dict
    dict_arcs = get_arcs_dict(name_arcs)

    # cut repeat vertices and return a list
    unique_vertices = get_unique_list(vertices)
    # Transform the vertices name to vertices id in unique_vertices
    arcs_list_unique = name_to_id(dict_arcs, unique_vertices)
    # Write result in file
    write_file_point("E:\\sil4_test\\test_unique_vertices", unique_vertices)
    write_file_arcs("E:\\sil4_test\\test_unique_arcs", arcs_list_unique)
