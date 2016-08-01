'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, total = '', 0, 0
        num = max(len(a), len(b))
        
        for i in range(num):
            if i < len(a):
                total += int(a[-(i+1)])
            if i < len(b):
                total += int(b[-(i+1)])
            carry, total = total / 2, total % 2
            result += str(total)
            total = carry
        if carry:
            result += str(carry)
        return result[::-1]

print(Solution().addBinary('1001','1011'))
