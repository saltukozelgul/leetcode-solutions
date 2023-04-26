class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return val if -2**31 <= val <= 2**31 - 1 else 0