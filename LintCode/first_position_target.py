class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binary_search(self, nums, target):
        # write your code here
        if nums:
            if target > nums[-1]:
                return -1
            elif target < nums[0]:
                return -1
            elif target == nums[0]:
                return 0
            elif target == nums[-1]:
                return len(nums) - 1
            else:
                left_edge = 0
                right_edge = len(nums) - 1
                while left_edge + 1 != right_edge:
                    divide = left_edge + (right_edge - left_edge) // 2
                    if target > nums[divide]:
                        left_edge = divide
                    elif target < nums[divide]:
                        right_edge = divide
                    else:
                        while True:
                            if nums[divide] == nums[divide - 1]:
                                divide -= 1
                            else:
                                break
                        return divide
                else:
                    return -1
        else:
            return -1


test = Solution()
print(test.binary_search([3, 4, 5, 8, 8, 8, 8, 10, 13, 14], 8))
