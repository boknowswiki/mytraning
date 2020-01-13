#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        n = len(nums)
        nums.sort()
        
        l = 0
        r = n - 1
        ret = 0
        
        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1
            else:
                ret += r - l
                r -= 1
                
        return ret
        
