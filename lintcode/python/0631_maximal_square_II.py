#!/usr/bin/python -t

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        # state: dp[i][j], number square at point [i,j], leftzero number zero to the left of [i,j],
        #           upzero[i][j] number zero to the up of [i,j]
        # function: dp[i][j] = min(dp[i-1][j-1], leftzero[i][j], upzero[i][j]) + 1
        # init: dp[i][j] = 0
        # result: ret*ret ret = max(ret, dp[i][j])
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        dp = [[0]*n for i in range(m)]
        left = [[0]*n for i in range(m)]
        up = [[0]*n for i in range(m)]
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                    up[i][j] = left[i][j] = 1
                    if i > 0:
                        up[i][j] = up[i-1][j] + 1
                    if j > 0:
                        left[i][j] = left[i][j-1] + 1
                else:
                    up[i][j] = left[i][j] = 0
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j-1], left[i][j-1], up[i-1][j]) +1
                    else:
                        dp[i][j] = 1
                
                ret = max(ret, dp[i][j])
                
        return ret * ret

