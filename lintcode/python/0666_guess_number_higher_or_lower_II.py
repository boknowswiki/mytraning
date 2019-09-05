#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class Solution:
    """
    @param n: An integer
    @return: how much money you need to have to guarantee a win
    """
    def getMoneyAmount(self, n):
        # write your code here
        #设dp[i][j]表示从区间[i,j]中猜中待猜数所需要的最小花费。
        #dp[i][j]=min\{k+max(dp[i][k-1],dp[k+1][j])\quad ||\quad i\leq k\leq j\}dp[i][j]=min{k+max(dp[i][k−1],dp[k+1][j])∣∣i≤k≤j}
        
        dp = [[0] * (n+1) for i in range(n+1)]
        
        for l in range(2, n+1):
            for i in range(1, n-l+2):
                j = l+i-1
                tmp = sys.maxint
                for k in range(i, j):
                    ret = k + max(dp[i][k-1], dp[k+1][j])
                    tmp = min(ret, tmp)
                    
                dp[i][j] = tmp
                
        return dp[1][n]


class Solution:
    """
    @param n: An integer
    @return: how much money you need to have to guarantee a win
    """
    def getMoneyAmount(self, n):
        # write your code here
        #设dp[i][j]表示从区间[i,j]中猜中待猜数所需要的最小花费。
        #dp[i][j]=min\{k+max(dp[i][k-1],dp[k+1][j])\quad ||\quad i\leq k\leq j\}dp[i][j]=min{k+max(dp[i][k−1],dp[k+1][j])∣∣i≤k≤j}
        
        dp = [[0] * (n+1) for i in range(n+1)]
        
        for l in range(2, n+1):
            for i in range(1, n-l+2):
                j = l+i-1
                if l == 2:
                    dp[i][j] = i
                    continue
                
                dp[i][j] = sys.maxint
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
                
        return dp[1][n]

