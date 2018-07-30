__author__ = 'Chanlone'


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if len(num) == 1:
            return num[0]
        start = 0
        end = len(num) - 1
        if num[start] < num[end]:
            return num[start]
        while (end - start) > 1:
            half = start + (end - start) // 2
            if num[start] < num[half]:
                start = half
            else:
                end = half
        return num[start] if num[start] < num[end] else num[end]


test = Solution()
print(test.findMin([1, 2, 3]))

