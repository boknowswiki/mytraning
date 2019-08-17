#!/usr/bin/python -t

# dp solution, time O(n), space O(1)

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        # state: dp[i] number of ways to paint at ith post
        # function: dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        # init: dp[0] = 0, dp[1] = k, dp[2] = k*k
        # result: dp[n-1]
        
        dp = [0, k, k*k, 0]
        if n <= 2:
            return dp[n]
        if k == 1:
            return 0
        
        for i in range(2, n):
            dp[3] = (dp[1]+dp[2]) * (k-1)
            dp[1] = dp[2]
            dp[2] = dp[3]
            
        return dp[3]

