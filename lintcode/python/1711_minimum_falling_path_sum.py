#!/usr/bin/python -t

# dp solution, zuobiao DP, time O(mn) space O(1)

class Solution:
    """
    @param A: the given array
    @return: the minimum sum of a falling path
    """
    def minFallingPathSum(self, A):
        # Write your code here
        # dp[i] the minimum sum at col i
        # dp[i] = min(dp[i-1], dp[i], dp[i+1]) + A[row][i]
        # ret = min(dp[i])
        
        if not A or not A[0]:
            return 0
            
        m = len(A)
        n = len(A[0])

        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    A[i][j] += min(A[i-1][j], A[i-1][j+1])
                elif j == n-1:
                    A[i][j] += min(A[i-1][j], A[i-1][j-1])
                else:
                    A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
                    
        return min(A[-1])

