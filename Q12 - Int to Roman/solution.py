class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # Conver the integer to a roman numeral
        # The idea is to use a greedy algorithm
        # We start with the largest roman numeral and keep subtracting it from
        # the integer until the integer is 0
        # We then move on to the next largest roman numeral
        # We keep track of the roman numerals we have used so far
        # We stop when the integer is 0


        # Create a list of roman numerals in descending order
        roman_numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV',
                            'I']
        # Create a list of integers in descending order
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        # Create a list to store the roman numerals
        roman_numeral_list = []
        # Create a variable to store the integer
        integer = num
        # Loop until the integer is 0
        while integer > 0:
            # Loop through the roman numerals
            for i in range(len(roman_numerals)):
                # If the integer is greater than or equal to the current roman
                # numeral, subtract the integer by the current roman numeral
                # and append the current roman numeral to the list
                if integer >= integers[i]:
                    integer -= integers[i]
                    roman_numeral_list.append(roman_numerals[i])
                    break
        
        return ''.join(roman_numeral_list)