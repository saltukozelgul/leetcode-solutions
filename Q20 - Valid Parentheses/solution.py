class Solution:
    def isValid(self, s: str) -> bool:
        

        # stack on python
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack.pop() != '(':
                    return False
                if i == '}' and stack.pop() != '{':
                    return False
                if i == ']' and stack.pop() != '[':
                    return False
        return not stack