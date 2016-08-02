'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, pairs = [], {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif not stack or char != stack.pop():
                return False
        if not stack: return True
        else: return False

print(Solution().isValid('[]}'))
