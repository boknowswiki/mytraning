#!/usr/bin/python -t

#time O(n) space O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = []
        p = 1
        
        for i in range(n):
            ret.append(p)
            p = p * nums[i]
        
        p = 1
        
        for i in range(n-1, -1, -1):
            ret[i] = ret[i]*p
            p = p * nums[i]
            
            
        return ret
