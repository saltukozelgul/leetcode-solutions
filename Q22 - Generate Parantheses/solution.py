class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # create a list to store all the results
        result = []

        current = ""
        left = 0
        right = 0

        # call the helper function
        self.helper(result, current, left, right, n)

        # return the result
        return result
    
    def helper(self, result, current, left, right, n):
        # if the length of current is 2 * n
        if len(current) == 2 * n:
            # append current to result
            result.append(current)
            return
        if left < n:
            # call the helper function with left + 1
            self.helper(result, current + "(", left + 1, right, n)
        if right < left:
            # call the helper function with right + 1
            self.helper(result, current + ")", left, right + 1, n)
