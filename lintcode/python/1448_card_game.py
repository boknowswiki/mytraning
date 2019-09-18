#!/usr/bin/python -t

# dp solution, beibao dp

class Solution:
    """
    @param n: The number of cards
    @param totalProfit: The totalProfit
    @param totalCost: The totalCost
    @param a: The profit of cards
    @param b: The cost of cards
    @return: Return the number of legal plan
    """
    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        # Write your code here
        MOD = 1000000007
        
        dp = [[[0] * (totalCost+1) for _ in range(totalProfit+2)] for _ in range(n+1)]
        dp[0][0][0] = 1
        
        for k in xrange(1, n+1):
            for i in xrange(totalProfit + 2):
                for j in xrange(totalCost):
                    if dp[k-1][i][j] == 0: continue
                    # not pick 
                    dp[k][i][j] = (dp[k][i][j] + dp[k-1][i][j]) % MOD
                    # pick
                    cost = j + b[k-1]
                    if cost < totalCost:
                        profit = min(i + a[k-1], totalProfit + 1)
                        dp[k][profit][cost] = (dp[k][profit][cost] + dp[k-1][i][j]) % MOD
        count = 0
        for j in xrange(totalCost):
            count = (count + dp[n][totalProfit+1][j]) % MOD 
        return count

