#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        n = len(nums)
        nums.sort()
        
        l = 0
        r = n-1
        ret = 0
        
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                l += 1
                r -= 1
                ret += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif val < target:
                l += 1
            else:
                r -= 1

        return ret
        
        
