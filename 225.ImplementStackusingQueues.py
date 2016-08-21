'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''
from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topnum = None
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.topnum = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        new = deque()
        if len(self.queue) == 1:
            self.queue.popleft()
            self.topnum = None
        elif len(self.queue) >= 2:
            while len(self.queue) > 2:
                new.append(self.queue.popleft())
            self.topnum = self.queue.popleft()
            new.append(self.topnum)
            self.queue = new        

    def top(self):
        """
        :rtype: int
        """
        return self.topnum

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

test = Stack()
test.push(1)
print(test.top())
