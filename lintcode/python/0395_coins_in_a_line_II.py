#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        # state: dp[i] is the max value the first player can have when there is i coins left
        # function: dp[i] = sum[i] - min(dp[i-1], dp[i-2])
        # init: sum[i] is the sum for i coins left
        # result: dp[n] > sum[n]/2
        
        n = len(values)
        sum_val = [0] *(n+1)
        
        for i in range(1, n+1):
            sum_val[i] = sum_val[i-1] + values[n-i]
            
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = values[n-1]
        
        for i in range(2, n+1):
            dp[i] = sum_val[i] - min(dp[i-1], dp[i-2])
            
        return dp[n] > sum_val[n]/2

