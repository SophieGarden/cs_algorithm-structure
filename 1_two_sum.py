'''
1. Two Sum
Easy

13414

490

Add to List

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i+1:]):
                if n1 + n2 == target:
                    return [i, i+1+j]
        return 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d.keys():
                return [d[n], i]
            else:
                d[target-n] = i

