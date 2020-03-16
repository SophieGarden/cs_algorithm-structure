18. 4Sum
Medium

1564

293

Add to List

Share
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Accepted
301,269
Submissions
923,211


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        d = {n:i for i, n in enumerate(nums)}
        seen = set()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k>j+1 and nums[k] == nums[k-1]:
                        continue
                    if target-nums[i]-nums[j]-nums[k] in d and d[target-nums[i]-nums[j]-nums[k]] > k:
                        seen.add((nums[i], nums[j], nums[k], target-nums[i]-nums[j]-nums[k]))

        return seen
        
