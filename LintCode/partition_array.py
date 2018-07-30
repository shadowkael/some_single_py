__author__ = 'lenovo'


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if nums:
            nums.sort()
            try:
                return nums.index(k)
            except ValueError:
                if nums[0] > k:
                    return 0
                else:
                    return len(nums)
        else:
            return 0


test = Solution()
print test.partitionArray([6, 6, 8, 6, 7, 9, 8, 7, 9, 6, 8, 6, 8, 9, 8, 7, 8, 6, 7, 6, 6, 8, 6, 6], 5)
