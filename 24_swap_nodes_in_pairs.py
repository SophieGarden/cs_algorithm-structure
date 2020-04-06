'''
24. Swap Nodes in Pairs
Medium

1847

156

Add to List

Share
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Accepted
421,283
Submissions
867,242
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next
            third = second.next
            prev.next = second
            second.next = first
            first.next = third
            prev = first
        return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first
        return second

