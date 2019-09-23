#!/usr/bin/python -t

# binary search solution, same as 0060

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        l = 0
        r = n - 1
        
        while l < r:
            mid = (l+r)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        if nums[l] == target:
            return l
        return -1

