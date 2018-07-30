class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        # write your code here
        if sorted(s) == sorted(t):
            return True
        else:
            return False
