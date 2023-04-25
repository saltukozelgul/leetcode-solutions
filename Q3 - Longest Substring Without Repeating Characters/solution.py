class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        longest = 0
        start = 0
        end = 0

        # Sliding window algorithm
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                longest = max(longest, end - start)
            else:
                char_set.remove(s[start])
                start += 1
        return longest
