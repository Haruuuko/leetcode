'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []: return [1]
        temp, l = 1, len(digits) - 1
        while l >= 0:
            if temp == 0:
                return digits[0 : l + 1] + digits[l + 1 :]
            addup = digits[l] + temp
            digits[l] = addup % 10
            temp = addup / 10
            l -= 1
        if temp == 1:
            return [1] + digits[:]
        return digits

print(Solution().plusOne([0]))

