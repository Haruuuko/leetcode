'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(rowIndex + 1):
            num = i - 1
            while num > 0: 
                result[num] += result[num - 1]
                num -= 1
            result.append(1)
        return result

print(Solution().getRow(3))

