#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
            
        return n-1

#time O(log2 ^ n) space O(1)

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
