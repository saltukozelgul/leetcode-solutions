class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Convert the roman numeral to an integer
        # The idea is to use a greedy algorithm
        # We start with the largest roman numeral and keep subtracting it from
        # the roman numeral until the roman numeral is empty
        # We then move on to the next largest roman numeral
        # We keep track of the integer we have seen so far
        # We stop when the roman numeral is empty

        roman_numerals = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,
                            'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        
        #sort the roman numerals in descending order
        roman_numerals = dict(sorted(roman_numerals.items(), key=lambda x: x[1], reverse=True))

        # Create a variable to store the integer
        integer = 0
        # Loop until the roman numeral is empty
        while len(s) > 0:
            # Loop through the roman numerals
            for roman_numeral in roman_numerals:
                # If the roman numeral starts with the current roman numeral,
                # subtract the roman numeral by the current roman numeral
                # and add the current integer to the integer
                if s.startswith(roman_numeral):
                    # Remove the current roman numeral from the roman numeral
                    s = s[len(roman_numeral):]
                    # Add the current integer to the integer
                    integer += roman_numerals[roman_numeral]
                    break
        return integer

sol = Solution()
print(sol.romanToInt(s='MCMXCIV'))