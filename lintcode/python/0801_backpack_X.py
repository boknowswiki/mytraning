#!/usr/bin/python -t

# dp solution, 01 beibao, time O(mn) space O(n)

class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        # write your code here
        # dp[i][j] for the ith merchandise and j yuan, it can parchase the goods

        
        prices = [150, 250, 350]
        m = 3
        
        dp = [0] * (n+1)
        
        for i in range(m):
            for j in range(prices[i], n+1):
                dp[j] = max(dp[j], dp[j-prices[i]]+prices[i])

        return n-dp[n]


# dp solution, duochong beibao

class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        # write your code here
        # dp[i][j] for the ith merchandise and j yuan, it can parchase the goods

        
        prices = [150, 250, 350]
        m = 3
        
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[0][0] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(j//(prices[i-1])+1):
                    if j >= k*prices[i-1] and dp[i-1][j-k*prices[i-1]]:
                        dp[i][j] = True
                        break
        
        for j in range(n, -1, -1):
            if dp[m][j]:
                return n-j
                
        return n


# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        # write your code here
        # dp[i][j] for the ith merchandise and j yuan, the max goods we can purchase
        # dp[i][j] = max(dp[i-1][j], dp[i][j-prices[i-1]]+prices[i-1]) 0<=i<=3
        # ret = n - dp[m][n]
        
        prices = [150, 250, 350]
        m = 3
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if j >= prices[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i][j-prices[i-1]]+prices[i-1])
                    
        return n-dp[m][n]

