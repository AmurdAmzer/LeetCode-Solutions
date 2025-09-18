'''Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false'''

# 1. Brute Force solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# 2. Optimal solution (Using a HashSet)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
