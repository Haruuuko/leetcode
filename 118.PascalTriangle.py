'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for i in range(1, numRows):
            result += [[1] + [result[i - 1][j] + result[i - 1][j + 1] for j in range(i - 1)] + [1]]
        return result

print(Solution().generate(3))
