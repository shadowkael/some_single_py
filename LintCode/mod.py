__author__ = 'lenovo'


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """

    def bitSwapRequired(self, a, b):
        c = a ^ b
        count = 0
        for i in range(32):
            mod = c % 2
            if mod == 1:
                count += 1
            c //= 2
        return count


test = Solution()
print test.bitSwapRequired(31, -14)
