#!/usr/bin/python -t

# dp solution, wanquan beibao, time O(mn) space O(n)

class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """
    def change(self, amount, coins):
        # write your code here
        # dp[i] the ways to get amount i
        # dp[j] += dp[j - coins[i]]
        # dp[amount]
        
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
                    
        return dp[amount]

