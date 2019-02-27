
1. Two Sum
Easy

9481

294

Favorite

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i




2. Add Two Numbers
Medium

4316

1044

Favorite

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy =  l3 = ListNode(0)
        carry = 0

        while l1 is not None or l2 is not None or carry:
            add = carry

            if l1 is not None:
                add += l1.val
                l1 = l1.next


            if l2 is not None:
                add += l2.val
                l2 = l2.next


            l3.next = ListNode(add%10)
            carry = add//10
            l3 = l3.next

        return dummy.next



3. Longest Substring Without Repeating Characters
Medium

4560

227

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        j = 0
        cur_set = set()
        max_len = 0
        while i < len(s) and j < len(s):
            if s[j] not in cur_set:
                cur_set.add(s[j])
                j += 1
                max_len  = max(max_len, j-i)
            else:
                cur_set.remove(s[i])
                i += 1
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        d = {}
        start = 0
        for i, char in enumerate(s):
            if char not in d:
                d[char] = i
            else:
                start = max(start, d[char] +1)
                d[char] = i


            max_len = max(max_len, i-start+1)

        return max_len
