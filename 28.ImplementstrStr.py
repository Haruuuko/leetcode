'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        h = len(haystack)
        if n > h:
            return -1
        else:
            for i in range(h - n + 1):
                part = haystack[i:i + n]
                if part == needle:
                    return i
        return -1
            
print(Solution().strStr('haystack','sta'))
