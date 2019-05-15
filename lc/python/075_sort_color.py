#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1
        i = 0
        
        while i < r+1:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                i = i + 1
                l = l + 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r = r - 1
            else:
                i = i + 1
                
        return
