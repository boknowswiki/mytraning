#!/usr/bin/python -t 

# time O(n)
# space O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        cur_min = prices[0]
        max_profit = 0

        for i in range(n):
            max_profit = max(max_profit, prices[i]-cur_min)
            cur_min = min(cur_min, prices[i])

        return max_profit

# dp solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        min_val = prices[0]
        ret = 0
        
        for i in range(1, n):
            min_val = min(min_val, prices[i])
            ret = max(ret, prices[i]-min_val)
            
        return ret

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
