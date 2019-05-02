#!/usr/bin/python -t

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

