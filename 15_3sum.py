15. 3Sum
Medium

5790

706

Add to List

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        list_3sum = []
        nums.sort()
        d = {n:i for i, n in enumerate(nums)}
        seen = set()
        for i, m in enumerate(nums):
            for j in range(i+1, len(nums)):
                n = nums[j]
                if -(m+n) in d and d[-(m+n)]>j:
                    seen.add((m, n, -(m+n)))
        return list(seen)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_3sum = []
        nums.sort()
        d = {n:i for i, n in enumerate(nums)}
        for i, m in enumerate(nums):
            if i>0 and m==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                n = nums[j]
                if j>i+1 and nums[j-1]==n:
                    continue
                if -(m+n) in d and d[-(m+n)]>j:
                    list_3sum.append([m, n, -(m+n)])
        # print(m, d2, list_3sum)
        return list_3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_3sum = []
        nums.sort()
        # d = {n:i for i, n in enumerate(nums)}
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        for i, m in enumerate(nums):
            if i>0 and m==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                n = nums[j]
                if j>i+1 and nums[j-1]==n:
                    continue
                if -(m+n) in d and d[-(m+n)]>j:
                    list_3sum.append([m, n, -(m+n)])
        # print(m, d2, list_3sum)
        return list_3sum

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        seen = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r < len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                if nums[l] + nums[r] == - n:
                    seen.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < - n:
                    l += 1
                else:
                    r -= 1
        return seen

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        seen = set()
        for i, n in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:

                if nums[l] + nums[r] == - n:
                    seen.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < - n:
                    l += 1
                else:
                    r -= 1
        return seen
