'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = []
        num, sign = '', '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            if i == len(s) - 1 or s[i] in '+-*/':
                print(s[i])
                if sign == '+':
                    stack.append(int(num))
                elif sign == '-':
                    stack.append(int(num) * (-1))
                elif sign == '*':
                    stack.append(stack.pop() * int(num))
                elif sign == '/':
                    stack.append(int(stack.pop() / float(num)))
                sign = s[i]
                num = ''
        result = 0
        print(stack)
        for n in stack:
            result += n
        return result

print(Solution().calculate('14-3/2'))
