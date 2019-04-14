#!/usr/bin/python -t

#time O(logn) space O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[mid] >= target and target >= nums[start]:
                    end = mid - 1
                else:
                    start = start + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

