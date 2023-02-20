#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        if target > nums[-1]:
            return n

        l = 0
        r = n-1

        while l + 1 < r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid

        if target <= nums[l]:
            return l

        return r

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


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            mid = (start+end)/2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return (start+1) if nums[start] < target else start


