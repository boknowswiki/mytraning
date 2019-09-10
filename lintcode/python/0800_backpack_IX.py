#!/usr/bin/python -t

# dp, time O(mn) space O(n)

class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        # write your code here
        #思想：反向思考（对问题做等价变换）
        #对于概率类问题，如果题目要求我们求一件事情成功的最大概率p，我们可以将其转化为求一件事情失败的最小概率p'，那么,1 - p'就是我们所求问题的答案。

        #分析：背包大小为总钱数，物品大小为各大学申请费，物品价值为大学录取率
        #状态：dp[i][j]申请前i个学校花费不超过j的一所没中的最小概率 => 一所没中的概率最小 => 中至少一所概率最大
        #转移方程：dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] * (1 - probability[i - 1])
        #初始条件：
        #dp[0][j] = 1 => 一所大学不申请，肯定中不上
        #dp[i][0] = 1, i != 0 => 申请至少一所大学不花钱，不可能
        #答案：1 - dp[m][n]
        
        # dp[i][j] the minimum probability for the first ith university, with j yuan, none of them gives offer
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-prices[i-1]*(1-probability[i-1])
        # dp[i][0] = 1, dp[0][j] = 1
        # ret = 1 - dp[m][n]
        
        m = len(prices)
        
        dp = [1.0] * (n+1)
        
        for i in range(1, m+1):
            for j in range(n, prices[i-1]-1, -1):
                dp[j] = min(dp[j], dp[j-prices[i-1]]*(1-probability[i-1]))
                    
        return 1-dp[n]

# dp solution, 01 beibao, MLE, time O(mn) space O(mn)

class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        # write your code here
        #思想：反向思考（对问题做等价变换）
        #对于概率类问题，如果题目要求我们求一件事情成功的最大概率p，我们可以将其转化为求一件事情失败的最小概率p'，那么,1 - p'就是我们所求问题的答案。

        #分析：背包大小为总钱数，物品大小为各大学申请费，物品价值为大学录取率
        #状态：dp[i][j]申请前i个学校花费不超过j的一所没中的最小概率 => 一所没中的概率最小 => 中至少一所概率最大
        #转移方程：dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] * (1 - probability[i - 1])
        #初始条件：
        #dp[0][j] = 1 => 一所大学不申请，肯定中不上
        #dp[i][0] = 1, i != 0 => 申请至少一所大学不花钱，不可能
        #答案：1 - dp[m][n]
        
        # dp[i][j] the minimum probability for the first ith university, with j yuan, none of them gives offer
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-prices[i-1]*(1-probability[i-1])
        # dp[i][0] = 1, dp[0][j] = 1
        # ret = 1 - dp[m][n]
        
        m = len(prices)
        
        dp = [[1.0] * (n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if j >= prices[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-prices[i-1]]*(1-probability[i-1]))
                    
        return 1-dp[m][n]

