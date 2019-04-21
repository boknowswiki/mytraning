#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        find = 0
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                find = 1
                break
                
        if find == 0 or i < 0:
            nums[:] = nums[::-1]
        else:
            for j in range(n-1, i, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[i+1:][::-1]
        return
