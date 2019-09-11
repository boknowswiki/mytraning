#!/usr/bin/python -t

# dp solution, time O(n) space O(1)

class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        # write your code here
        n = len(prices)
        
        sell = 0
        buy = -prices[0]
        
        for i in range(1, n):
            buy = max(buy, sell-prices[i])
            sell = max(sell, buy+prices[i]-fee)
            
        return sell


# dp solution, MLE, time O(n) space O(n^2)

class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        # write your code here
        # almost the same as 0995 with cooldown
        n = len(prices)
        
        dp = [[0] * n for i in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]-fee)
            
        return dp[n-1][1]

