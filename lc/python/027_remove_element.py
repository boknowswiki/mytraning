#!/usr/bin/python -t

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != val:
                if i != index:
                    nums[index] = nums[i]
                index = index + 1
        
        return index

