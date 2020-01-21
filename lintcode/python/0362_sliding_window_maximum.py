#!/usr/bin/python -t

# two pointers


import collections

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        n = len(nums)
        
        q = collections.deque([])
        
        ret = []
        
        if n == 0 or k == 0:
            return ret
            
        for i in range(n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
                
            q.append(i)
            
            if i+1 >= k:
                ret.append(nums[q[0]])
                
            if i+1-k == q[0]:
                q.popleft()
                
        return ret
        
        
