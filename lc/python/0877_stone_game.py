#!/usr/bin/python -t

# leetcode solution

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        if n == 0:
            return True
        
        dp = [[0] * (n+2) for i in range(n+2)]

        
        for s in range(1, n+1):
            for i in range(n-s+1):
                j = i + s - 1
                parity = (j+i+n)%2
                if parity == 1:
                    dp[i+1][j+1] = max(piles[i]+dp[i+2][j+1], piles[j]+dp[i+1][j])
                else:
                    dp[i+1][j+1] = min(-piles[i]+dp[i+2][j+1], -piles[j]+dp[i+1][j])
        
        return dp[1][n] > 0

# dp solution, time O(n^3), hit TLE
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        if n == 0:
            return True
        
        dp = [[0] * n for i in range(n)]
        val = [[0] * n for i in range(n)]
        v = [[0] * n for i in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                val[i][j] = val[i][j-1] + piles[j]
                
        return self.dfs(0, n-1, dp, val, v)
    
    def dfs(self, l, r, dp, val, v):
        if v[l][r]:
            return dp[l][r]
        
        dp[l][r] = sys.maxint
        
        for i in range(l, r):
            dp[l][r] = min(dp[l][r], self.dfs(l, i, dp, val, v) +
                                self.dfs(i+1, r, dp, val, v)) + val[l][r]
            
        v[l][r] = 1
        return dp[l][r]

