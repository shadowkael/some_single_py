__author__ = 'lenovo'
import os

ROOT_DIR = 'E:\\sil4_test\\test_sil4_data'
SYSTEM_CALL_LIST = os.listdir(ROOT_DIR)
os.chdir(ROOT_DIR)
NEST_SPACE = 2


def walk_system_call_list():
    for system_call in SYSTEM_CALL_LIST:
        process_dir = ROOT_DIR + "\\" + system_call + "\\sys_tree"
        if os.path.isdir(process_dir):
            os.chdir(process_dir)
        else:
            continue
        log_line = dict()
        for log_and_sys_tree in sorted(os.listdir(os.getcwd())):
            if not os.path.isfile(os.getcwd() + "\\" + log_and_sys_tree):
                continue
            # count every weight of sys_tree and store in log_line
            if log_and_sys_tree.endswith("log"):
                log_line[log_and_sys_tree.split('_')[0]] = get_line_num(log_and_sys_tree)
            # write contact of vertices
            elif log_and_sys_tree.startswith('sys'):
                target_file_name = 'R_' + log_and_sys_tree + '.net'
                sys_tree_num = log_and_sys_tree.split('_')[-1]
                data_format(log_and_sys_tree, target_file_name, log_line[sys_tree_num])
    pass


def data_format(format_file, target_file, sys_tree_weight):
    with open(format_file, 'r') as sil4_data:
        data_copy = sil4_data.readlines()
        arcs_list = list()
        for index, data_out_line in enumerate(data_copy):
            # Count space in each line
            space_out_num = get_space_num(data_out_line)
            # judge each line nest
            data_inner = data_copy[index + 1:]
            for inner_index, data_inner_line in enumerate(data_inner):
                space_inner_num = get_space_num(data_inner_line)
                if space_out_num == space_inner_num - NEST_SPACE:
                    item_content = "\t" + str(index + 1) + " " + str(index + 1 + inner_index + 1) + " " + str(
                        sys_tree_weight) + "\n"
                    arcs_list.append(item_content)
                    # output_function(index, inner_index + 1)
                elif space_out_num >= space_inner_num:
                    break
        # write .net data in file
        write_file_head(target_file, len(data_copy))
        write_file_point(target_file, data_copy)
        write_file_arcs(target_file, arcs_list)
    print "Success"


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
    with open(graph_file, 'w') as file_head:
        head_str = "*Vertices\t" + str(point_num) + "\n"
        file_head.write(head_str)


def write_file_point(graph_file, points):
    with open(graph_file, 'a') as file_points:
        for index, point in enumerate(points):
            points_str = "\t" + str(index + 1) + " " + '"' + point.strip() + '"' + "\n"
            file_points.write(points_str)


def write_file_arcs(graph_file, arcs):
    with open(graph_file, 'a') as file_arcs:
        file_arcs.write("*Arcs\n")
        for i in arcs:
            file_arcs.write(i)


if __name__ == "__main__":
    walk_system_call_list()
