'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        prestr = ''
        start = strs[0]
        for i in range(len(start)):
            char = start[i]
            for str_ in strs:
                if i > len(str_) - 1 or char != str_[i]:
                    return prestr
            prestr += char

        return prestr

print(Solution().longestCommonPrefix([]))
