'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
import re
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = {}
        less = []
        res = 0
        for i in s:
            if dic.has_key(i): dic[i] += 1
            else: dic[i] = 1
        for key in dic:
            if dic[key] < k: less.append(key)
        if not less: return len(s)
        split = re.split('|'.join(less), s)
        for substr in split:
            if len(substr) >= k:
                res2 = self.longestSubstring(substr, k)
                res = max(res, res2)
        return res

print(Solution().longestSubstring('ababbc', 2))
