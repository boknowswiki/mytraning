#!/usr/bin/python -t

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n -1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid+1

        return start

