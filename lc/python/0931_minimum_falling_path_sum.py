#!/usr/bin/python -t

# dp
# time O(mn)
# space O(mn)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] the min sum at (i, j)
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        # dp[i][j] = matrix[i][j]
        # return min(matrix[m-1])
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1] if j > 0 else sys.maxsize, matrix[i-1][j+1] if j < n-1 else sys.maxsize )

        return min(matrix[m-1])

# dp time O(m*n) space O(1), modified on A.

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        if m == 0:
            return 0
        
        n = len(A[0])
            
        for i in range(m-2, -1, -1):
            for j in range(n):
                A[i][j] = min(A[i+1][j-1] if j>=1 else sys.maxint,
                              A[i+1][j], 
                              A[i+1][j+1] if j<=n-2 else sys.maxint) + A[i][j]
        
        return min(ret for ret in A[0])

# my dp solution time O(m*n) space O(m*n)
# state: dp[i][j] the minimum sum at point i, j
# function: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + A[i][j]
# init: dp[0][j] = A[0][j] for the first row
# result: min(dp[m-1][j] for j in range(n))

import sys

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        if m == 0:
            return 0
        
        n = len(A[0])
        
        dp = [[sys.maxint] * (n) for i in range(m)]
        for j in range(n):
            dp[0][j] = A[0][j]
        
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min(dp[i-1][j] if i>=1 else sys.maxint,
                              dp[i-1][j-1] if i>= 1 and j >= 1 else sys.maxint,
                              dp[i-1][j+1] if i >= 1 and j<=n-2 else sys.maxint) + A[i][j]
        print dp
        
        return min(ret for ret in dp[m-1])

if __name__ == '__main__':
    s = [[1,2,3],[4,5,6],[7,8,9]]
    ss = Solution()
    print('answer is %r' % ss.minFallingPathSum(s))
