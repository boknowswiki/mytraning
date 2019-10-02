#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        lo = self.lower_bound(nums, target)
        hi = self.upper_bound(nums, target)
        
        if nums[lo] != target:
            return [-1, -1]
        return [lo, hi]
        
        
    def lower_bound(self, nums, target):
        r = len(nums)-1
        l= 0
        
        while l < r:
            mid = (l+r)/2
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
                
        return l
        
        
    def upper_bound(self, nums, target):
        r = len(nums)-1
        l = 0
        
        while l < r:
            mid = (l+r)/2
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid
                
        return l-1

