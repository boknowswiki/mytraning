#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        nums.sort()
        num_set = set(nums)
        ret = 0
        
        for num in nums:
            if num - target in num_set:
                ret += 1
                
        return ret
        

# two pointers


class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        n = len(nums)
        if n <= 1:
            return 0
            
        nums.sort()
        result = 0 
        i = 0
        for j in range(n):
            while i < j and nums[j] - nums[i] > target:
                i += 1
            if nums[j] - nums[i] == target:
                result += 1
                i += 1
        return result
