#!/usr/bin/python -t

# dp solution, time O(n) space O(1)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # state: dp[i] max profit when we sell on ith day
        # function: dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])
        # init: dp[0] = 0
        # result: ret = max(ret, dp[i])
        
        n = len(prices)
        if n == 0:
            return 0
        
        max_profit = 0
        min_val = prices[0]
        ret = 0
        
        for i in range(1, n):
            min_val = min(min_val, prices[i-1])
            max_profit = prices[i] - min_val
            ret = max(ret, max_profit)
        return ret


# dp solution, time O(n) space O(n)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # state: dp[i] max profit when we sell on ith day
        # function: dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])
        # init: dp[0] = 0
        # result: ret = max(ret, dp[i])
        
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [0] * n
        ret = 0
        
        for i in range(1, n):
            dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])
            ret = max(ret, dp[i])
            
        return ret

