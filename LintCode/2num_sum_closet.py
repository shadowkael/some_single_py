__author__ = 'lenovo'


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """

    def twoSum(self, numbers, target):
        # write your code here
        num_sum = []
        for outer_index, outer_num in enumerate(numbers):
            if outer_num == numbers[outer_index - 1]:
                continue
            for inner_index, inner_num in enumerate(numbers):
                if inner_index == outer_index:
                    continue
                else:
                    if target == outer_num + inner_num:
                        if outer_index > inner_index:
                            outer_index, inner_index = inner_index, outer_index
                        return [outer_index + 1, inner_index + 1]

        num_sum = list(set(num_sum))
        print num_sum
        abs_num = 0
        while True:
            for num in num_sum:
                if abs_num == abs(num - target):
                    return num
            else:
                abs_num += 1


test = Solution()
print test.twoSum([1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2], 7)
