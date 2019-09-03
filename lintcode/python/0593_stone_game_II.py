#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        # write your code here
        # dp[i][j] from i to j the minimum score
        # dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum(j-i))
        
        n = len(A)
        
        if n <= 1:
            return 0
            
        dp = [[0] * (2*n) for i in range(2*n)]
        s = [0]* (2*n+1)
        
        # sum of first ith pils
        for i in range(1, 2*n+1):
            s[i] = s[i-1] + A[(i-1)%n]
            
        for i in range(2*n):
            dp[i][i] = 0
            
        for l in range(2, 2*n+1):
            for i in range(0, min(2*n, 2*n-l+1)):
                j = l + i - 1
                dp[i][j] = sys.maxint
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j] + s[j+1]-s[i])
                    
        ret = sys.maxint
        for i in range(n):
            ret = min(ret, dp[i][i+n-1])
                
        return ret

