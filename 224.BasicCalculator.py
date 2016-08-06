'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        number, operators = [], []
        lst = self.makelist(s)
        for i in range(len(lst)):
            if lst[i].isdigit():
                number.append(int(lst[i]))               
            elif lst[i] in '+-*/':
                while operators and self.pri(lst[i]) <= self.pri(operators[-1]):
                    self.compute(number, operators)
                operators.append(lst[i])
            elif lst[i] == '(':
                operators.append(lst[i])
            elif lst[i] == ')':
                while operators[-1] != '(':
                    self.compute(number, operators)
                operators.pop()            
        while operators:
             self.compute(number, operators)

        return number[0]

    def pri(self, char):
        if char =='(':
            return -1
        elif char in '+-':
            return 0
        elif char in '*/':
            return 1
        elif char in ')':
            return 2
        return 0

    def makelist(self, s):
        slist = []
        temp = ''
        for i in range(len(s)):
            if s[i].isdigit():
                temp += s[i]
                if i < len(s) - 1 and not s[i + 1].isdigit() or i == len(s) - 1:
                    slist.append(temp)
                    temp = ''
            elif s[i] in '+-*/()':
                slist.append(s[i])
        print(slist)
        return slist

    def compute(self, num, op):
        if not op: return 0
        b, a = num.pop(), num.pop()
        operator = op.pop()
        print(a, operator, b)
        if operator == '+':
            num.append(a + b)
        elif operator == '-':
            num.append(a - b)
        elif operator == '*':
            num.append(a * b)
        elif operator == '/':
            num.append(a / b)

print(Solution().calculate('(1+(4+5+2)-3)+(6+8)'))
