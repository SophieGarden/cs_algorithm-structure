'''21. Merge Two Sorted Lists
Easy

3497

519

Add to List

Share
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = l3 = ListNode(-1)
        while l1 is not None or l2 is not None:
            if l1 is None or (l1 is not None and l2 is not None and l1.val > l2.val):
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
            else:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
        return dummy.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = prev = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return dummy.next
            
