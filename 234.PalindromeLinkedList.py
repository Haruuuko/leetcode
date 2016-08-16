'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return True

        fast, slow, reverse, temp = head, head.next, head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            temp = reverse
            reverse = slow
            slow = slow.next
            reverse.next = temp
        if not fast.next:
            reverse = reverse.next

        while slow:
            if slow.val != reverse.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True
            
