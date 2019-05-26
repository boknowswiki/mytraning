#!/usr/bin/python -t

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return nums[i]
            
        return -1

#another way to use hashtable to check
