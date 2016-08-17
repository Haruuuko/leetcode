'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        slow, fast = head, head.next
        while slow and fast and slow is not fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        return True if slow is fast else False        
