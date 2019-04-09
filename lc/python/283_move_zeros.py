#!/usr/bin/python -t

#Time O(n) space O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        index = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index = index + 1
                
        return
