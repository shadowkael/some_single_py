__author__ = 'lenovo'


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        num_sum = []
        numbers.sort()
        for outer_index, outer_num in enumerate(numbers):
            if outer_num == numbers[outer_index - 1]:
                continue
            for inner_index, inner_num in enumerate(numbers):
                # if inner_num == numbers[inner_index - 1]:
                #     continue
                if inner_index == outer_index:
                    continue
                else:
                    for third_index, third_num in enumerate(numbers):
                        if third_num == numbers[third_index - 1]:
                            continue
                        if third_index == outer_index or third_index == inner_index:
                            continue
                        else:
                            num_sum.append(outer_num + inner_num + third_num)

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
print test.threeSumClosest([1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2], 7)
