class Solution:
    def fibonacci(self, n):
        # write your code here
        if n >= 2:
            return Solution.fibonacci(
                self, n - 1) + \
                   Solution.fibonacci(
                       self, n - 2)
        elif n == 1:
            return 1
        else:
            return 0

if __name__ == "__main__":
    solution = Solution()
    print solution.fibonacci(20)
