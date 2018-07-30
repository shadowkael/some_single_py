__author__ = 'lenovo'


def threeNumClosest(numbers, target):
    # write your code here
    if len(numbers) <= 3:
        return sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    abs_max_num = abs(max_num - target) if abs(max_num - target) > abs(min_num - target) else abs(min_num - target)
    three_nums = []

    def add_same_num(num):
        if numbers.count(num) > 1:
            while len(three_nums) < 3:
                three_nums.append(num)

    for i in range(abs_max_num + 1):
        if len(three_nums) >= 3:
            return sum(three_nums)
        if target + i in numbers:
            three_nums.append(target + i)
            add_same_num(target + i)

        if target - i in numbers:
            three_nums.append(target - i)
            add_same_num(target - i)

import cProfile
cProfile.run('3num_sum_closet')
# print threeNumClosest([-2, -3, -4, -5, -100, 99, 1, 4, 4, 4, 5, 1, 0, -1, 2, 3, 4, 5], 77)
