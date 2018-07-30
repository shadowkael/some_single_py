__author__ = 'lenovo'


def productExcludeItself(A):
    # write your code here
    B = list()
    length_a = len(A)
    if length_a <= 1:
        B = [1]
        return B
    left_case_list = list()
    right_case_list = list()
    for (left_item, right_item) in zip(A, reversed(A)):
        if left_case_list and right_case_list:
            left_case_list.append(left_case_list[-1] * left_item)
            right_case_list.append(right_case_list[-1] * right_item)
            pass
        else:
            left_case_list.append(left_item)
            right_case_list.append(right_item)

    for i in range(length_a):
        left_window = i - 1
        right_window = length_a - i - 2
        if left_window < 0:
            left_num = 1
        else:
            left_num = left_case_list[left_window]
        if right_window < 0:
            right_num = 1
        else:
            right_num = right_case_list[right_window]
        B.append(left_num * right_num)
    return B


print productExcludeItself([1, 2, 3])
