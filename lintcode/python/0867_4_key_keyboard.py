#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

#获得最优解的按键序列一定可以用以下两种子序列拼接而成:
#
#数个连续的 A
#Ctrl-A + Ctrl-C + 数个连续的 Ctrl-V
#设定状态: f[i] 表示i次按键可以获得的最多数量的A
#
#我们的决策便是选用上面两种方案的哪一种, 枚举即可
#
#状态转移方程:
#
#f[i] = max( f[i-1] + 1, f[i-2-j] * (j+1) )
#需要枚举j, 含义是连续按下了多少个 Ctrl-V
#
#边界: f[i] = i, i <= 4

class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        # write your code here
        # dp[i] the max number of A can get at ith time the key pressed.
        # dp[i] = max(dp[i-1]+1, dp[i-1+(j+1)]*(j+1), j is how many times we pressed ctrl+ v
        # or dp[i] = max(dp[i-1]+1, dp[j]*(i-j-1))
        # dp[0] = 1
        # dp[n-1]
        
        dp = [0] * N
        dp[0] = 1
        
        for i in range(1, N):
            dp[i] = dp[i-1] + 1
            for j in range(i-3):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
                
        return dp[N-1]

