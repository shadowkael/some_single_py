__author__ = 'lenovo'


class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        cmp_value = A[1]
        for index, value in enumerate(A[1:]):
            if cmp_value == value:
                continue
            if cmp_value > A[index + 1]:
                return index
            else:
                cmp_value = A[index + 1]


test = Solution()
print test.findPeak(
    [683, 800, 926, 1710, 99, 1939, 1186, 690, 595, 180, 200, 992, 502, 921, 191, 38, 717, 817, 368, 551, 950, 618, 915,
     40, 452, 266, 416, 991, 44, 946, 261, 829, 8, 460, 118, 883, 418, 209, 483, 500, 492, 912, 421, 347, 233, 50, 33,
     781, 277, 282, 700, 786, 987, 831, 964, 82, 153, 827, 289, 47, 451, 967, 622, 202, 429, 268, 42, 682, 857, 41, 412,
     427, 909, 699, 214, 519, 758, 12, 57, 193, 961, 724, 40, 857, 532, 183, 75, 688, 764, 729, 718, 929, 6, 13, 878,
     788, 15, 862, 227, 619, 104])
