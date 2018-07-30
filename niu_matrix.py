# coding=utf-8
import sys


# 该问题相当于是问起点的可达点中最长路径是多少

if __name__ == "__main__":
    try:
        while True:
            input_data = sys.stdin.readline().strip()
            if not input_data:
                break
            row = int(input_data[0])
            col = int(input_data[1])
            matrix = []
            for r in range(row):
                matrix.append(sys.stdin.readline().strip())
            k = int(sys.stdin.readline().strip())
            rules = []
            for rule in range(k):
                rules.append(sys.stdin.readline().strip())
            rules = [int(rule) for rule in rules]
    except:
        pass
