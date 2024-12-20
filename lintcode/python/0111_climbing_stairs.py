#!/usr/bin/python -t

# dp, time O(n), space O(1)

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        # state: dp[i], distinct ways to reach ith stair
        # function: dp[i] = dp[i-1]+dp[i-2]
        # init: dp[0] = 0, dp[1] = 1, dp[2] = 2
        # result: dp[n]
        
        if n < 3:
            return n
            
        last = 1
        lastlast = 1
        now = 0        
        for i in range(2, n+1):
            now = last + lastlast
            lastlast = last
            last = now
            
        return now

# dp solution, time O(n), space O(n)

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        # state: dp[i], distinct ways to reach ith stair
        # function: dp[i] = dp[i-1]+dp[i-2]
        # init: dp[0] = 0, dp[1] = 1, dp[2] = 2
        # result: dp[n]
        
        dp = [0] * (n+1)
        
        if n < 3:
            return n
            
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]+ dp[i-2]
            
        return dp[n]

