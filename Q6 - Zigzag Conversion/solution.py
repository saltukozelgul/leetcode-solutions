class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        res = ""
        for x in range(numRows):
            inc = 2 * (numRows - 1)
            for i in range(x, len(s), inc):
                res += s[i]
                if x != 0 and x != numRows - 1 and i + inc - 2 * x < len(s):
                    res += s[i + inc - 2 * x]

        return res