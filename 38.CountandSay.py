'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def countNext(n):
            if n < 1:
                return '0'
            elif n == 1:
                return '1'
            else:
                str_ = countNext(n-1)
                num, result = str_[0], ''
                count = 0
                for char in str_:
                    if char == num:
                        count += 1
                    else:
                        result += str(count) + num
                        num = char
                        count = 1
                result += str(count) + num
                return result
        return countNext(n)

print(Solution().countAndSay(9))
