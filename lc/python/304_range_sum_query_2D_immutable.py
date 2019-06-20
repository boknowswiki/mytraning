#!/usr/bin/python -t

#time O(mn) space O(mn)
#myself solution

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            self.dp = []
            return
        n = len(matrix[0])
        self.dp = [[0] * (n+1) for _ in range(m+1)]
        #self.dp[0][0] = matrix[0][0]
        
        #for i in range(1, m):
        #    self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
            
        #for j in range(1, n):
        #    self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]
        
        for i in range(0, m):
            for j in range(0, n):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] - self.dp[i][j] + matrix[i][j]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]
