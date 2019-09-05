#!/usr/bin/python -t

# dp solution, time O(mn) space O(m)

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        # dp[i][j] the minimum coins for first i coins at j amount of money
        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-k*coins[i]+k)
        
        n = len(coins)
        
        dp = [sys.maxint] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
                
        return dp[amount] if dp[amount] != sys.maxint else -1

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        # dp[i][j] the minimum coins at i coins for j amount money
        # dp[i][j] = min(dp[i-1][j], dp[i][j-k*coins[i]]+k) 0<=k*coins[i] <= j
        # dp[i][j] = 0
        
        n = len(coins)
        
        dp = [[sys.maxint]*(amount+1) for i in range(n+1)]
        dp[0][0] = 0
        
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                
                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)
                    
        return dp[n][amount] if dp[n][amount] != sys.maxint else -1

