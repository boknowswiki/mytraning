#!/usr/bin/python -t

# binary search solution, time O(logn) space O(1)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        l = 0
        r = n - 1
        
        while l < r:
            mid = (l+r)/2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
                
        if nums[l] == target:
            return l
            
        if nums[l-1] == target:
            return l-1
        
        return -1

