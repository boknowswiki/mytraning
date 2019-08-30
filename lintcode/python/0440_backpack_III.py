#!/usr/bin/python -t

# time O(mn) space O(m)

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        # dp[i], maximum value can put into size i
        
        n = len(A)
        dp = [0] * (m+1)
        
        for i in range(n):
            for j in range(A[i], m+1):
                dp[j] = max(dp[j], dp[j-A[i]]+V[i])
                
        return dp[m]


#比较简单的转移是直接枚举第i种物品取用多少个: f[i][j] = max{f[i - 1][j - x * A[i]] + x * V[i]}
#
#但是这样速度较慢, 可以优化成 f[i][j] 直接由 f[i][j - A[i]] 转移, 并且从小到大枚举 j, 这样做的含义就是在已经拿过第 i 个物品的之后还可以再拿它. 也就是说: 计算 f[i][j] 时, 初始设置为 f[i - 1][j], 然后 f[i][j] = max(f[i][j], f[i][j - A[i]] + V[i])
#
#另外, 可以使用滚动数组优化, 使用滚动数组之后也不必要手动设置 f[i][j] = f[i - 1][j], 与01背包使用的滚动数组相反, 这里恰好需要正着枚举容量 j, 因而有 f[j] = max(f[j], f[j - A[i]] + V[i])

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        # state: dp[i][j], for the first i type of items, with size j, the max value we can get
        # function: dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]]+V[i-1]) if j >= A[i-1] else dp[i][j] = dp[i-1][j], this is different than backpack II, since the i type item can have multiple
        # init: dp[i][j] = 0
        # result: dp[n][m]
        n = len(A)
        
        dp = [[0] * (m+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]]+ V[i-1])
                    
        return dp[n][m]


# dp solution time O(n^2) space O(n)

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        f = [0 for i in xrange(m+1)]
        for (a, v) in zip(A, V):
            for j in xrange(a, m+1):
                if f[j - a] + v > f[j]:
                    f[j] = f[j - a] + v
        return f[m]
