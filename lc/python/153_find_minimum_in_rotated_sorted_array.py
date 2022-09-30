#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = n-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
                
        if nums[r] < nums[l]:
            return nums[r]
        return nums[l]

#time O(logn) space O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            mid = (start+end)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]

