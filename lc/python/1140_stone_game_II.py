#!/usr/bin/python -t

# dp solution time O(n^3) space O(n^2)
# https://leetcode.com/problems/stone-game-ii/discuss/345247/C%2B%2B-DP-(Tabulation)

# state: dp[i][j] is the maximum number of stones Alex can get when starting at index i with M = j
# sum_val[i] is the total number of stones from index i to the end
# The dp matrix for Lee is the same. And the stragegy for Alex is to choose an optimal X to minimize the number of stones Lee can get when starting at index (i + X) with M = max(X,j). Here we have the recurrence formula

# function : dp[i][j] = max(dp[i][j], sum_val[i] - dp[i + X][max(j, X)]) where 1<= X <= 2j;

# init: dp[i][n] = sum_val[i]
# result dp[0][1]

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        dp = [[0] * (n+1) for i in range(n+1)]
        sum_val = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            sum_val[i] = sum_val[i+1] + piles[i]
            
        for i in range(n+1):
            dp[i][n] = sum_val[i]
            
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                for x in range(1, 2*j+1):
                    if i+x > n:
                        break
                    dp[i][j] = max(dp[i][j], sum_val[i] - dp[i + x][max(j, x)])
                    
        return dp[0][1]

