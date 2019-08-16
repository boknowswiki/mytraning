#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        # state: dp[i], the number of ways to get to ith stair
        # function: dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        # init: dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = 4
        # result: dp[n]
        
        if n == 0:
            return 1
        if n < 3:
            return n
            
        dp = [0] * (n+1)
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            
        return dp[n]

