class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.myAtoi(x)

    def myAtoi(self,x):
        isNegative = False
        string = ""
        showSign = False
        for i in str(x):
            if i == "-" and string == "" and not showSign:
                isNegative = True
            elif i.isdigit():
                string += i
            elif i == " ":
                continue
            elif i == "+" and string == "":
                showSign = True
                continue
            else:
                break

        if string == "":
            return 0
        val = int(string)
        if isNegative:
            val = -val
        if val > 2**31 - 1:
            return 2**31 - 1
        elif val < -2**31:
            return -2**31
        else:
            return val


            
