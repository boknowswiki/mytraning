#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: the given sequence
    @return: the length of the longest subsequence that is a wiggle sequence
    """
    def wiggleMaxLength(self, nums):
        # Write your code here
        # p[i] the max longest subsequence at i for increasing
        # q[i] the max longest subsequence at i for decreasing
        # if increasing, p[i] = (p[i],q[j]+1) if decreasing q[i] = max(q[i], p[j]+1), 0<=j<i
        # ret = max(p[n],q[n])
        
        n = len(nums)
        
        p = [1] * (n+1)
        q = [1] * (n+1)
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    p[i] = max(p[i], q[j]+1)
                if nums[i] < nums[j]:
                    q[i] = max(q[i], p[j]+1)
                    
        return max(p[n-1], q[n-1])

