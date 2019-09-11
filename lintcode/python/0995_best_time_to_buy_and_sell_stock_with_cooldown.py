#!/usr/bin/python -t

#dp solution, time O(n) space O(n)

class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def maxProfit(self, prices):
        # write your code here
        # dp[i][j], means for ith day, the maximum profit on j == 0 for buy, j == 1, for sell
        # for buy on ith day, dp[i][0] = max(dp[i-1][0], dp[i-2][1]-prices[i] if i >= 2 else 0 - prices[i])
        # for sell on ith day, dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        # dp[n-1][1]
        
        n = len(prices)
        
        sell = [0] * n
        buy = [0] * n
        cd = [0] * n
        
        buy[0] = -prices[0]
        
        for i in range(1, n):
            cd[i] = sell[i-1]
            buy[i] = max(buy[i-1], cd[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            #sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            #buy[i] = max(buy[i - 1], cd[i - 1] - prices[i])
            
        #return max(sell[-1], cd[-1])
        return sell[-1]


# dp solution, zuobiao, MLE, time O(n) space O(n^2)

class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def maxProfit(self, prices):
        # write your code here
        # dp[i][j], means for ith day, the maximum profit on j == 0 for buy, j == 1, for sell
        # for buy on ith day, dp[i][0] = max(dp[i-1][0], dp[i-2][1]-prices[i] if i >= 2 else 0 - prices[i])
        # for sell on ith day, dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        # dp[n-1][1]
        
        n = len(prices)
        
        dp = [[0] * n for i in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1]-prices[i] if i >= 2 else 0 - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            
        return dp[n-1][1]

