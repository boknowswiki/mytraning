#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        n = len(nums)
        ret = 0
        nums.sort()
        l = 0
        r = n-1
        
        while l < r:
            val = nums[l] + nums[r]
            if val <= target:
                ret += r-l
                l += 1
            else:
                r -= 1
                
        return ret
                
