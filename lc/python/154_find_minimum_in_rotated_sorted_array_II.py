#!/usr/bin/python -t

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

