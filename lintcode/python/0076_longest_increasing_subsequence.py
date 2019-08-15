#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        # state: dp[i] the longest increasing subsequence number at i
        # function: dp[i] = max(dp[i], dp[j]+1) when nums[i] > nums[j]
        # init: dp[i] = 1
        #result: dp[n-1]
        n = len(nums)
        if n < 2:
            return n
            
        dp = [1] * n
        ret = dp[0] = 1
        
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                
            ret = max(ret, dp[i])
            
        return ret

