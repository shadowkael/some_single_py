class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        # write your code here
        def get_divide_len(now_len):
            get_len = 0
            for stock in L:
                get_len += stock // now_len
            return get_len

        if L:
            L.sort(reverse=True)
            if k <= L.__len__():
                if L[0] // 2 < L[k - 1]:
                    return L[k - 1]
            if L[0] >= k:
                divide_num = k + 1
            else:
                divide_num = L[0] + 1
            for num in range(2, divide_num):
                max_len = L[0] // num
                divide_len = get_divide_len(max_len)
                if divide_len == k:
                    return max_len
                elif divide_len > k:
                    edge = L[0] // (num - 1) + 1
                    for require_len in xrange(edge, max_len, -1):
                        divide_len = get_divide_len(require_len)
                        if divide_len >= k:
                            return require_len
                    else:
                        return max_len
        else:
            return 0
        return 0


PATH = 'E:\\PycharmProjects\\some_single_py\\LintCode\\test\\stock8.in'


def get_list(path):
    with open(PATH, 'rt') as list_file:
        list_in = list_file.read()
        return list_in


list_data = eval(get_list(PATH))
test = Solution()
print test.woodCut(list_data, 9000)
