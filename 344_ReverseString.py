'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s_array = list(s)

        while i < j:
            s_array[i], s_array[j] = s_array[j], s_array[i]
            i += 1
            j -= 1
        return ''.join(s_array)

