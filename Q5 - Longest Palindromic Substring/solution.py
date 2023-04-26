class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        dp is bool array that shows if substring from i to j is palindrome
        dp[i][j] = True if s[i:j+1] is palindrome
        dp[i][j] = False otherwise
        """

        n = len(s)
        longest = ""
        dp = [[False] * n for _ in range(n)]

        # All one-letter substrings are palindromes
        # we are doing it for avoid unnecessary checks
        for i in range(n):
            dp[i][i] = True
            longest = s[i]

        # Check all longer substrings
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if len(s[i:j+1]) > len(longest):
                        longest = s[i:j+1]

        return longest
