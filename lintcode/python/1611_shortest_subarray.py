#!/usr/bin/python -t

# pre sum solution

class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of shortest subarray
    """
    def smallestLength(self, nums, k):
        # Write your code here
        n = len(nums)
        ret = sys.maxint
        sum = j = 0
        for i in range(n):
            while j < n and sum < k:
                sum += nums[j]
                j += 1
                
            if sum >= k:
                ret = min(ret, j-i)
            sum -= nums[i]
                
        return ret if ret != sys.maxint else -1

