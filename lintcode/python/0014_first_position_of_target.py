#!/usr/bin/python -t

# binary search solution, time O(logn) space O(1)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        # find lower_bound

        n = len(nums)
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
                
        return -1 if nums[l] != target else l

