#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        n = len(nums)
        ret = sys.maxint
        
        left = 0
        right = 0
        val = 0
        
        for right in range(n):
            val += nums[right]
            while val >= s:
                ret = min(ret, right-left+1)
                val -= nums[left]
                left += 1
                
        return ret if ret != sys.maxint else -1
        
        
