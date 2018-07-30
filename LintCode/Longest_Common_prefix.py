__author__ = 'lenovo'


class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        strs.sort()
        LCP = ''
        for index, char_item in enumerate(strs[0]):
            for str_item in strs[1:]:
                if str_item[index] == char_item:
                    continue
                else:
                    return LCP
            LCP += char_item
        return LCP


if __name__ == "__main__":
    solution = Solution()
    print solution.longestCommonPrefix(['abcddff', 'abdddd', 'abccc', 'ab'])
