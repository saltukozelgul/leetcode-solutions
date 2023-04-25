class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ## Sliding window algorithm
        longest = 0
        longestString = ""
        start = 0
        end = 0
        while end < len(s):
            if self.isPalindrome(s[start:end+1]):
                end += 1
                if end - start > longest:
                    longest = end - start
                    longestString = s[start:end]
            else:
                start += 1

    def isPalindrome(self, s):
        return s == s[::-1]

