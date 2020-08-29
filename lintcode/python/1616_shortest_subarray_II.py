#!/usr/bin/python -t


import collections

class Solution:
    """
    @param nums: 
    @param k: 
    @return: return the length of subarray
    """
    def smallestLengthII(self, nums, k):
        # Write your code here
        n = len(nums)
        if n == 0:
            return -1
            
        pre_sum = [0] * (n+1)
        
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
            
        ret = n+1
        q = collections.deque()
        
        for i in range(n+1):
            while q and pre_sum[i] - pre_sum[q[0]] >= k:
                ret = min(ret, i-q.popleft())
            while q and pre_sum[i] <= pre_sum[q[-1]]:
                q.pop()
            
            q.append(i)
            
        return ret if ret != n+1 else -1
