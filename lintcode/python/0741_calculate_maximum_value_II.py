#!/usr/bin/python -t

# dp solution, qujian DP, time O(n^2) space O(n^2)

class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def maxValue(self, str):
        # write your code here
        # dp[i][j] the maximum value from [i,j]
        # dp[i][j] = max(dp[i][k]+dp[k+1][j], dp[i][k]*dp[k+1][j])
        # dp[i][i] = int(str[i])
        # dp[0][n-1]
        
        n = len(str)
        
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = int(str[i])
            
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l+i-1
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j], dp[i][k]*dp[k+1][j])
                    
        return dp[0][n-1]

