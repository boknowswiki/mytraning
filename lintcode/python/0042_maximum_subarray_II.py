#!/usr/bin/python -t

# dp solution

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)
        
        l_lmax = [0] * n
        l_gmax = [0] * n
        
        l_lmax[0] = l_gmax[0] = nums[0]
        
        for i in range(1, n):
            l_lmax[i] = max(l_lmax[i-1]+nums[i], nums[i])
            l_gmax[i] = max(l_gmax[i-1], l_lmax[i])
            
        r_lmax = [0] * n
        r_gmax = [0] * n
        
        r_lmax[n-1] = r_gmax[n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            r_lmax[i] = max(r_lmax[i+1]+nums[i], nums[i])
            r_gmax[i] = max(r_gmax[i+1], r_lmax[i])
            
        max_val = -sys.maxint
        
        for i in range(1, n):
            max_val = max(l_gmax[i-1] + r_gmax[i], max_val)
            
        return max_val
