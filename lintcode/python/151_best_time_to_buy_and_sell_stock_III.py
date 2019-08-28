#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # left[i] is the max profit at ith day from left side
        # right[i] is the max profit at ith day from right side
        # left[i] = max(left[i-1], l_min)
        # right[i] = max(right[i+1, r_max)
        # ret = max(ret, left[i]+right[i])
        
        n = len(prices)
        if n == 0:
            return 0
            
        left = [0] * (n)
        right = [0] * (n)
        l_min = prices[0]
        r_max = prices[n-1]
        
        for i in range(1, n):
            l_min = min(l_min, prices[i])
            left[i] = max(left[i-1], prices[i]-l_min)
            
        for i in range(n-2, -1, -1):
            r_max = max(r_max, prices[i])
            right[i] = max(right[i+1], r_max-prices[i])
        
        ret = 0
        for i in range(1, n):
            ret = max(ret, left[i]+right[i])
            
        return ret


# general solution, but Memory Limit Exceeded
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        
        K=2
        if K >= n/2:
            profit = 0
            for i in range(1, n):
                diff = prices[i] - prices[i-1]
                if diff > 0:
                    profit += diff
                    
            return profit
        
        globalbest = [[0] * (n+1) for i in range(n+1)]
        mustsell = [[0] * (n+1) for i in range(n+1)]
        
        for i in range(n+1):
            globalbest[0][i] = mustsell[0][i] = 0
            
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            mustsell[i][0] = 0
            for j in range(1, K+1):
                mustsell[i][j] = max(mustsell[i-1][j]+diff, globalbest[i-1][j-1]+diff)
                globalbest[i][j] = max(globalbest[i-1][j], mustsell[i][j])
                
        return globalbest[n-1][K]

