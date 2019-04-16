#!/usr/bin/python -t 

#time O(n) space O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        max_val = 0
        min_val = prices[0]
        
        for i in range(1, n):
            if prices[i] < min_val:
                min_val = prices[i]
                continue
            if prices[i] - min_val > max_val:
                max_val = prices[i] - min_val
                
        return max_val
