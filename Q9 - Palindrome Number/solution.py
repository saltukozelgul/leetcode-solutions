class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Can we say python is cheating? xd
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]