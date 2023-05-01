class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ## This code is still not working for all cases
        ## I will come back to this later
        
        if s == p:
            return True
        
        if "." not in p and "*" not in p:
            return s == p
        

        i = 0
        j = 0
        for i in range(len(s)):
            if s[i] == p[j] or p[j] == '.':
                i += 1
                j += 1
            elif p[j] == '*':
                if s[i] == p[j-1] or p[j-1] == '.':
                    i += 1
                    j += 1
            elif j < len(p) - 1 and p[j+1] == '*':
                j += 2
            else:
                return False
        return True