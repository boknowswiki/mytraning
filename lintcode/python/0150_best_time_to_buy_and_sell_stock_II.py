#!/usr/bin/python -t

# greedy time O(n) space O(1)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        diff = profit = 0
        n = len(prices)
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
                
        return profit

