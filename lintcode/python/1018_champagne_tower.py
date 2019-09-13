#!/usr/bin/python -t

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param poured: an integer
    @param query_row: an integer
    @param query_glass: an integer
    @return: return a double
    """
    def champagneTower(self, poured, query_row, query_glass):
        # write your code here
        # dp[i][j] how full at i row, j glass
        # dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] - 2.0)/2.0
        # dp[n][n] if dp[n][n] <= 1 else 1

        dp = [[0.0 for _ in range(i)] for i in range(1, query_row+2)]
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                if dp[i][j] > 1:
                    dp[i+1][j] += (dp[i][j]-1)/2.0
                    dp[i+1][j+1] += (dp[i][j]-1)/2.0
                    
        return float(dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1)

