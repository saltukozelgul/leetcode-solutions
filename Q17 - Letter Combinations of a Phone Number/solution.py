class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        number_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if digits == '':
            return []
        
        if len(digits) == 1:
            return number_to_letters[digits[0]]

        result = []
        for letter in number_to_letters[digits[0]]:
            for combination in self.letterCombinations(digits[1:]):
                result.append(letter + combination)
        
        return result
