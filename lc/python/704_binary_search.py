#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        return -1

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

