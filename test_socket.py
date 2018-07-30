# coding=utf-8
__author__ = 'lenovo'

import sys


def check_num(num):
    for i in range(2, num / 2):
        if num % i:
            continue
        else:
            return False
    else:
        return True


print check_num(200)

if __name__ == "__main__":
    while True:
        input_data = raw_input()
        if not input_data:
            break

        light_coordinates = raw_input().split()
        if not light_coordinates:
            break
        light_coordinates.extend([1, input_data.split()[-1]])
        light_coordinates = [int(i) for i in light_coordinates]
        light_coordinates.sort()
        max_div = 0
        for index in range(1, len(light_coordinates)):
            new_div = light_coordinates[index] - light_coordinates[index - 1]
            if new_div > max_div:
                max_div = new_div
        print '%.2f' % (max_div/2.0)
