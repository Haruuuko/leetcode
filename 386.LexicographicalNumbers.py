'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        i = 1
        while True:
            result.append(i)
            if i * 10 <= n:
                i *= 10
            else:
                while i % 10 == 9 or i == n:
                    i /= 10
                if i == 0:
                    return result
                i += 1
print(Solution().lexicalOrder(38))
