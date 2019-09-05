#!/usr/bin/python -t

# dp solution, time O(mnk) space O(mnk)

class Solution:
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """
    def findMaxForm(self, strs, m, n):
        # write your code here
        # dp[i][j][k] for first i strings, j 0, k 1, the maximum number can fit
        # dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros(strs[i])][k-ones(strs[i])+1)
        
        l = len(strs)
        dp = [[[0]*(n+1) for j in range(m+1)] for i in range(l+1)]
        
        for i in range(1, l+1):
            cost = self.cnt(strs[i-1])
            for j in range(m+1):
                for k in range(n+1):
                    if j >= cost[0] and k >= cost[1]:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-cost[0]][k-cost[1]]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
                        
        return dp[l][m][n]
            
    def cnt(self, s):
        cost = [0, 0]
        
        for i in s:
            if i == '0':
                cost[0] += 1
            else:
                cost[1] += 1
                
        return cost

