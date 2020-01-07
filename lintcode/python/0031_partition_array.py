#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
            
        index = 0
        
        for i in range(n):
            if nums[i] < k:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
                
        return index
        
