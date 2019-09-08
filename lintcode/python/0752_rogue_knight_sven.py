#!/usr/bin/python -t

# dp solution, zuobiao, time O(n^2m) space O(nm)

class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """
    def getNumberOfWays(self, n, m, limit, cost):
        # 
        # dp[i][j] means ways of from planet 0 to i, with j gold coins left
        # dp[i][j] = dp[k][j+cost[i]] for k from i-limit <= k < i, and j+cost[i] <= m
        # dp[0][m] = 1, dp[0][0]...dp[0][m-1] = 0
        # ret = dp[n][j] 0<=j<=m
        
        dp = [[0] * (m+1) for i in range(n+1)]
        dp[0][m] = 1
        
        for i in range(n+1):
            for j in range(m+1):
                for k in range(max(i-limit, 0), i):
                    if j+cost[i] <= m:
                        dp[i][j] += dp[k][j+cost[i]]
            
        ret = 0
        for j in range(m+1):
            ret += dp[n][j]
            
        return ret

