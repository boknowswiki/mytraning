#!/usr/bin/python -t

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        
        for i in range(1, n):
            if nums[index] != nums[i]:
                index = index + 1
                nums[index] = nums[i]
        return index+1

