'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        number = ''
        i, sign = 0, 1
        while i < len(str):
            if str[i] == ' ':
                i += 1
            elif str[i] == '-':
                if i < len(str) - 1 and not str[i + 1].isdigit(): break
                sign = -1
                count = 1
                i += 1
            elif str[i] == '+':
                if i < len(str) - 1 and not str[i + 1].isdigit(): break
                count = 1
                i += 1
            elif not str[i].isdigit():
                break
            else:
                number += str[i]
                if i < len(str) - 1 and not str[i + 1].isdigit(): break
                i += 1

        if len(number) == 0: 
            return 0
        elif sign * int(number) > INT_MAX:
            return INT_MAX
        elif sign * int(number) < INT_MIN:
            return INT_MIN
        else: 
            return sign * int(number)

print(Solution().myAtoi(' -0012a42'))

