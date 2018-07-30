class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if A:
            if target <= A[0]:
                return 0
            elif target >= A[-1]:
                return len(A)
            else:
                left_edge = 0
                right_edge = len(A)
                while left_edge != right_edge - 1:
                    divide = left_edge + int((right_edge - left_edge) // 2)
                    if target > A[divide]:
                        left_edge = divide
                    elif target < A[divide]:
                        right_edge = divide
                    else:
                        return divide + 1
                else:
                    return left_edge + 1
        else:
            return 0


test = Solution()
print test.searchInsert([1, 3, 5, 6, 8, 9], 7)
