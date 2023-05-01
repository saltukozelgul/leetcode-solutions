class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Create a variable to store the longest common prefix
        longest_common_prefix = ''
        # Loop through the characters in the first string
        for i in range(len(strs[0])):
            # Loop through the strings
            for j in range(1, len(strs)):
                # If the character at the current index in the first string
                # is not equal to the character at the current index in the
                # current string, return the longest common prefix
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return longest_common_prefix
            # Add the character at the current index in the first string to
            # the longest common prefix
            longest_common_prefix += strs[0][i]
        return longest_common_prefix