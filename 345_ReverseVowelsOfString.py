'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s_array = list(s)
        vowel = 'aeiou'

        while i < j:
            if not s_array[i].lower() in vowel:
                i += 1
            if not s_array[j].lower() in vowel:
                j -= 1
            if s_array[i].lower() in vowel and s_array[j].lower() in vowel:
                s_array[i], s_array[j] = s_array[j], s_array[i]
                i += 1
                j -= 1
        return ''.join(s_array)

