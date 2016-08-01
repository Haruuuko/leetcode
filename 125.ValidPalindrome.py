'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True

        newlist = []
        for char in s:
            if char.isalnum():
                newlist.append(char.lower())
        
        i, j = 0, len(newlist) - 1
        while i < j:
            if newlist[i] != newlist[j]:
                return False
            i, j = i + 1, j - 1
        return True

print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
