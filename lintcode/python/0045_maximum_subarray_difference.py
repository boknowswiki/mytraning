#!/usr/bin/python -t

#dp solution

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        
        l_max = [0] * n
        l_min = [0] * n
        r_max = [0] * n
        r_min = [0] * n
        
        local_max = local_min = nums[0]
        l_max[0] = l_min[0] = nums[0]
        
        for i in range(1, n):
            local_max = max(nums[i], local_max+nums[i])
            l_max[i] = max(l_max[i-1], local_max)
            local_min = min(nums[i], local_min+nums[i])
            l_min[i] = min(l_min[i-1], local_min)
        
        local_max = local_min = nums[n-1]    
        r_max[n-1] = r_min[n-1] = nums[n-1]
        
        for i in range(n-2, -1, -1):
            local_max = max(nums[i], local_max+nums[i])
            r_max[i] = max(r_max[i+1], local_max)
            local_min = min(nums[i], local_min+nums[i])
            r_min[i] = min(r_min[i+1], local_min)
            
        diff = 0
        
        for i in range(n-1):
            diff = max(abs(l_max[i]-r_min[i+1]), diff)
            diff = max(abs(l_min[i]-r_max[i+1]), diff)
            
        return diff;

