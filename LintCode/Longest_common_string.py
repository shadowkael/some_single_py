__author__ = 'lenovo'
from sys import argv


class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        C = str()
        D = str()
        if len(A) <= len(B):
            C = A
            D = B
        else:
            C = B
            D = A
        print C, A
        for num in range(len(C)):
            substr_list = list()
            window = len(C) - num
            head = 0
            tail = window
            substr_list.append(C[head:tail])
            while (tail < len(C)):
                head += 1
                tail += 1
                substr_list.append(C[head:tail])

            for item in substr_list:
                if D.find(item) != -1:
                    print D.find(item)
                    return D.find(item)


if __name__ == '__main__':
    solution = Solution()
    # print solution.longestCommonSubstring(argv[1], argv[2])
    print solution.longestCommonSubstring('', '')
