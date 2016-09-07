'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return ""
        num, string = [], []
        last = ''
        for i in s:
            if i.isdigit():
                if last.isdigit():
                    num[-1] = num[-1]*10 + int(i)
                else:
                    num.append(int(i))
            elif i.isalpha():
                if last.isalpha() or last == ']':
                    string[-1] = string[-1] + i
                else:
                    string.append(i)
            elif i == ']':
                s2 = string.pop() * num.pop()
                if string: string[-1] += s2
                else: string.append(s2)
            last = i
        if len(string) == 1:
            return string.pop()
        else:
            return string[0] + string[1]

print(Solution().decodeString('sd2[f2[e]g]i'))

