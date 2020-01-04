#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return
        
        odd = 0
        
        for i in range(n):
            if nums[i] % 2:
                nums[odd], nums[i] = nums[i], nums[odd]
                odd += 1
                
        return
    

