#!/usr/bin/python -t

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        n = len(nums)
        l = 0
        t = -sys.maxint
        s = 0
        
        for r in range(n):
            s = s + nums[r]
            
            if r - l + 1 == k:
                t = max(t, s)
                s -= nums[l]
                l += 1
                
        return t * 1.0/k
