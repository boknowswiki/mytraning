#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # dp[i][j] means the sum from [0,0] to [i,j]
        # dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+matrix[i][j]
        
        if not matrix or (not matrix[0]):
            return
        
        m = len(matrix)
        n = len(matrix[0])
        
        self.dp = [[0] * (n+1) for i in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

