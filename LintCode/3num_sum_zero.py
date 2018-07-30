__author__ = 'Chanlone Gogh'


class Solution:
    """
    @param numbers : Give an array numbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        result = []
        for first_index, first_num in enumerate(numbers[:-2]):
            for second_index, second_num in enumerate(numbers[first_index + 1:]):
                for third_index, third_num in enumerate(numbers[first_index + second_index + 2:]):
                    if first_num + second_num + third_num:
                        continue
                    else:
                        result.append((first_num, second_num, third_num))
        result = list(set(result))
        return result


test = Solution()
from pprint import pprint

pprint(test.threeSum([-1, 0, 1]))
