#!/usr/bin/python -t

#dp solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        
        for i in range(n-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
                
        return profit

# one pass solution
# time O(n) space O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_val = 0
        
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max_val += prices[i] - prices[i-1]
                
        return max_val

#time O(n) space O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        valley = prices[0]
        peak = prices[0]
        max_sum = 0
        i = 0
        
        while i < (n-1):
            while (i < n-1) and (prices[i] >= prices[i+1]):
                i = i + 1
            valley = prices[i]
            
            while (i < n-1) and (prices[i] <= prices[i+1]):
                i = i + 1
                
            peak = prices[i]
            
            max_sum = max_sum + (peak - valley)
            
        return max_sum


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])

