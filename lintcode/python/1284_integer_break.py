#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param n: a positive integer n
    @return: the maximum product you can get
    """
    def integerBreak(self, n):
        # Write your code here
        # dp[i] means the max product can get at number i after breaking to at least two positive integers
        # dp[i] = max(dp[i], dp[i-j]*j) 0<j<i
        # ret = dp[n]
        
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            dp[i] = i
            if i == n:
                dp[i] = 0
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j)
                
        return dp[n]

