#!/usr/bin/python -t

# time O(n^2m) space O(n)

class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        # write your code here
        # dp[i][j] the maximum weight with ith items and j yuan
        # dp[i][j] = max(dp[i-1][j-k*prices[i-1]+weight[i-1]*k, dp[i][j]), 0<=k<=amounts
        # dp[i][j] = 0
        # dp[m][n]
        
        f = [0 for x in range(n + 1)]
        m = len(prices)
        for i in range(m):
            for j in range(1, amounts[i] + 1):
                for k in range(n + 1)[::-1]:
                    if k >= prices[i]:
                        f[k] = max(f[k], f[k - prices[i]] + weight[i])
        return f[n]


# dp solution, wanquan beibao zhuan 01 beibao, time O(n^2m) space O(mn)

class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        # write your code here
        # dp[i][j] the maximum weight with ith items and j yuan
        # dp[i][j] = max(dp[i-1][j-k*prices[i-1]+weight[i-1]*k, dp[i][j]), 0<=k<=amounts
        # dp[i][j] = 0
        # dp[m][n]
        
        m = len(prices)
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(1, amounts[i-1]+1):
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j >= k*prices[i-1]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-k*prices[i-1]]+k*weight[i-1])
                        
        return dp[m][n]

