#!/usr/bin/python -t

# dp solution, time O(nk) space O(n^2)

class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        #globalbest[i][j] 表示前i天，至多进行j次交易时的最大获益
        #mustsell[i][j] 表示前i天，至多进行j次交易，并且第i天卖出手中的股票时的最大获益
        #状态转移:

        #mustsell[i][j] = max(globalbest[i - 1][j - 1], mustsell[i - 1][j]) + prices[i] - prices[i - 1]
        #globalbest[i][j] = max(globalbest[i - 1][j], mustsell[i][j])
        #边界: mustsell[0][i] = globalbest[0][i] = 0
        # result: globalbest[n-1][k]
        
        n = len(prices)
        
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
            
