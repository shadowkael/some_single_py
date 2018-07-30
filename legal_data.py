__author__ = 'lenovo'

TARGET_PATH = 'D:\\gcl\\common\\future_net\\asset\\case4\\topo_format_4.txt'
DEMAND_PATH = 'D:\\gcl\\common\\future_net\\asset\\case4\\demand.csv'

if __name__ == "__main__":
    with open(TARGET_PATH, 'r') as graph_data:
        with open(DEMAND_PATH, 'r') as vertices:
            vertices_str = vertices.readlines()
            vertices_num = vertices_str[0].split('|')
            vertices_num[0] = vertices_num[0].split(',')[-1]
            for num in range(0, vertices_num.__len__()):
                if vertices_num[num] not in vertices_str:
                    print "Elegiac"
                    print num
                    print vertices_num[num]

scan = 'I could see no valley, no farms, no cottages and no church spire--only a lake.'
