#!/usr/bin/python -t

# qujian dp
# time O(n^2)

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
            
        n = len(values)
        dp = [[0] * n for _  in range(n)]
        sum = [[0] * n for _  in range(n)]
        
        for i in range(n):
            dp[i][i] = values[i]
            sum[i][i] = values[i]
        
        for i in range(n - 2, -1, -1):  # n-2 => 0
            for j in range(i + 1, n):  # i+1 => n-1
                sum[i][j] = sum[i + 1][j] + values[i]
                dp[i][j] = sum[i][j] - min(dp[i + 1][j], dp[i][j - 1])
                
        return dp[0][n - 1] > sum[0][n - 1] - dp[0][n - 1]
