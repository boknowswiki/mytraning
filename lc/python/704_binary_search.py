#!/usr/bin/python -t

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        
        while l < r:
            m = l+(r-l)/2
            if nums[m] < target:
                l = m+1
            else:
                r = m
                
        return l if nums[l] == target else -1

