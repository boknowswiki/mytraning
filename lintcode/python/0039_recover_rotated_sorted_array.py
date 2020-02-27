#!/usr/bin/python -t

# binary search
# time O(n) worse case

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i+1, n-1)
                self.reverse(nums, 0, n-1)
                
        return
    
    
    def reverse(self, nums, l, r):
        if l >= r:
            return
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        return
    
