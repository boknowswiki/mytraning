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
        l = 0
        r = n-1
        
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1
            
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
        return l
        

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
        
