#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 2
        
        for i in range(2, n):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index = index + 1
                
        return index
