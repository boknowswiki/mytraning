#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        n = len(nums)
        
        index = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
                
        return
    
