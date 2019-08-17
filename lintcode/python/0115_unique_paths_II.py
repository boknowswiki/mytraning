#!/usr/bin/python -t

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        # state: dp[i][j] unique paths at point [i, j]
        # function: obstacleGrid[i][j] != 1 and dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # init: dp[0][0] = 1
        # result: dp[m-1][n-1]
        
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] != 1 else 0
            
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] != 1 else 0
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
                        
        return dp[m-1][n-1]

