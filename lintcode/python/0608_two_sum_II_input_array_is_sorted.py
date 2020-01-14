#!/usr/bin/python -t

# two pointers, binary search

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        n = len(nums)
        l = 0
        r = n-1
        
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                return [l+1, r+1]
            elif val < target:
                l += 1
            else:
                r -= 1
                
        return [-1,-1]
        
        
