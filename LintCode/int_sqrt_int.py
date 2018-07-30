class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x == 1:
            return 1
        for i in xrange(x):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
            else:
                continue


test = Solution()
print(test.sqrt(100))
