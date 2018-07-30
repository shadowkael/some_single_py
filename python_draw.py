class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        if len(A) <= 1:
            return len(A)
        head = 0
        count = 0
        abc = list()
        abc.extend(A)
        for index in range(1, len(A)):
            if A[index] == A[head]:
                continue
            elif A[index] > A[head]:
                head += 1
                count += 1
                if head == index:
                    continue
                A[head] = A[head] ^ A[index]
                A[index] = A[head] ^ A[index]
                A[head] = A[head] ^ A[index]
                continue
            elif A[index] < A[head]:
                break

        a = list()
        return count + 1


solution = Solution()
# with open('F:\\chrom_down\\4.in', 'r') as process_list:
#     process_str = process_list.readlines()[0]
process_str = [-10, 0, 1, 2, 3]
# process_str = [-14, -14, -13, -13, -13, -13, -13, -13, -13, -12, -12, -12, -12, -11, -10, -9, -9, -9, -8, -7, -5, -5,
#                -5, -5, -4, -3, -3, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5,
#                5, 5, 6, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 14, 14, 14, 14, 15, 16,
#                16, 16, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 23, 23, 24,
#                25, 25]
print solution.removeDuplicates(
    process_str)
