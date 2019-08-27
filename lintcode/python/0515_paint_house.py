#!/usr/bin/python -t

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        #用坐标型动态规划做很好理解。用dp[i][0]表示油漆到第i栋房子，且第i栋房子用红色的花费
        # state: dp[i][j] for ith house with color j, the minimum cost for the first i houses
        # function is :
        # dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
        # dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
        # dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costs[i-1][2]
        # init: dp[i][j] = 0
        # result dp[n][i] for i in [0,2] the minimum value
        
        n = len(costs)
        dp = [[0] * 3 for i in range(n+1)]
            
        for i in range(1, n+1):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costs[i-1][2]
            
                        
        return min(dp[-1])

# dp solution, time O(nk^2) space O(nk)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        # state: dp[i][j] for ith house with color j, the minimum cost for the first i houses
        # function: dp[i][j] = min(dp[i-1][k]) + cost[i][j] k != j
        # init: dp[i][j] = 0
        # result dp[n][i] for i in [0,2] the minimum value
        
        n = len(costs)
        dp = [[0] * 3 for i in range(n+1)]
            
        for i in range(1, n+1):
            for j in range(3):
                dp[i][j] = sys.maxint
                for k in range(3):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i-1][j])
                        
        ret = sys.maxint
        for i in range(3):
            ret = min(ret, dp[n][i])
            
        return ret

