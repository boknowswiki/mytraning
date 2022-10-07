#!/usr/bin/python -t

# binary search
# time worst O(n), normal O(logn)
# space O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[r] == nums[mid]:
                r -= 1
            elif nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
                
        if nums[l] <= nums[r]:
            return nums[l]
        return nums[r]
    

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        while start < end and nums[start] >= nums[end]:
            mid = (start+end)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
            else:
                start = start + 1

        return nums[start]


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
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end = end - 1
                
        return nums[start]
