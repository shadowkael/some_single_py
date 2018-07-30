__author__ = 'lenovo'


def permutation(perm, or_list, n):
    if n == len(or_list):
        perm.append(or_list)
        # print(perm)

    for i in range(n, len(or_list)):
        or_list[i], or_list[n] = or_list[n], or_list[i]
        permutation(perm, or_list, n + 1)
        or_list[i], or_list[n] = or_list[n], or_list[i]


perm = []
permutation(perm, [1, 2, 3], 0)
print perm
