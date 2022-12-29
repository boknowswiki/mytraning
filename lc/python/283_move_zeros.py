#!/usr/bin/python -t

# two pointers

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        index = 0

        for i in range(n):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        while index < n:
            nums[index] = 0
            index += 1

        return

#Time O(n) space O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        index = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index = index + 1
                
        return
