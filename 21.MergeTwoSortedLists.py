'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = self
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return self.next

    def mergeTwoListsRecursive(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2

l1 = ListNode(2)
l2 = ListNode(1)
res = Solution().mergeTwoLists(l1, l2)
print(res.val, res.next.val)
