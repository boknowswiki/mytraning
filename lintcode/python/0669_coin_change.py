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

