#!/usr/bin/python -t

# dp solution

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def quicksolv(prices, n):
            profit = 0
            
            for i in range(1, n):
                if prices[i] - prices[i-1] > 0:
                    profit += prices[i] - prices[i-1]
                    
            return profit
            
        n = len(prices)
        if n == 0:
            return 0
        
        if k >= n/2:
            return quicksolv(prices, n)
        
        dp = [0] * (k+1)
        min_dp = [prices[0]] * (k+1)
        
        for i in range(1, n):
            for t in range(1, k+1):
                min_dp[t] = min(min_dp[t], prices[i]-dp[t-1])
                dp[t] = max(dp[t], prices[i]-min_dp[t])
                
        return dp[k]

