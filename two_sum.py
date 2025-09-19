# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

#  1. Brute Force Solution (Time O(n^2); space O(1))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target) and (i != j):
                    return [i, j]

# 2. HashMap Solution (Time O(n); space O(n))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {} # value : index

        for i, num in enumerate (nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i

