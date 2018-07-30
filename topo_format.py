__author__ = 'lenovo'

SOURCE_PATH = 'D:\\gcl\\common\\future_net\\asset\\case4\\topo.csv'
TARGET_PATH = 'D:\\gcl\\common\\future_net\\asset\\case4\\topo_format.txt'


def read_file(file_path):
    with open(file_path, 'r') as graph_description:
        graph_list = graph_description.readlines()
        graph_str = graph_list[0][:-1]
        for i in graph_list[1:]:
            i = ',' + i[:-1]
            graph_str += i
        return graph_str


def write_file(file_path, str_data):
    with open(file_path, 'w') as grapth_format:
        grapth_format.write(str_data)


if __name__ == "__main__":
    write_file(TARGET_PATH, read_file(SOURCE_PATH))
