'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        lines = [''] * numRows

        for i in range(len(s)):
            rem = i % (2 * numRows - 2)
            if rem < numRows:
                lines[rem] += s[i]
            else:
                lines[2 * numRows - 2 - rem] += s[i]
        return ''.join(lines[n] for n in range(numRows))

print(Solution().convert('PAYPALISHIRING', 3))
