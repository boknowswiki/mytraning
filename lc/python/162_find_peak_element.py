#!/usr/bin/python -t

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        
        while start < end:
            mid = (start+end)/2
            
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid
                
        return start
