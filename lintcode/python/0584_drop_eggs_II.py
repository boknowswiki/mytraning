#!/usr/bin/python -t

# dp solution, time O(mn^2) space O(mn)

#动态规划思想
#状态：题目问啥状态就是啥，有i个鸡蛋，确认在第j层鸡蛋会不会坏的最坏情况下需要丢的次数。
#转移方程：
#dp[i][j] = min( dp[i][j], 1 + Math.max( dp[i - 1][k - 1], dp[i][j - k] ) )
#想象你有n个鸡蛋和h层尚待试验。然后你从这h层里的第i层丢鸡蛋
#如果鸡蛋坏了：
#问题变成n-1个鸡蛋和i-1层楼尚待实验（因为i楼坏了，往更高的楼层肯定都会坏，只有往下试验）
#如果鸡蛋没坏：
#问题变成n个鸡蛋和h-i层楼尚待试验。
#
#问题中重要的不是h这个总楼层，而是还有多少层楼需要试验。
#比如说测试1到20层楼和测试21到40层楼其实是一样的。
#
#这里就可以定义dp[i][j]了，在最坏情况拿下，用n个鸡蛋，以及最少的丢的次数， 找到是哪一个楼层k，会让鸡蛋摔碎。
#即：dp[i][j] = 1 + Math.max( dp[i - 1][k - 1], dp[i][j - k] )
#
#初始状态:
#因为我们需要丢h次，如果只有一个鸡蛋的话。所以dp[1][h] = h
#因为不管有多少鸡蛋，我们至少需要丢一次才知道k是不是1层，所以的dp[i][1] = 1
#因为0层不需要丢，所以dp[i][0] = 0

class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        # write your code here
        # dp[i][j], for i eggs, at j floor the minimum number of drops
        # dp[i][0] = 0, dp[i][1] = 1, dp[1][j] = j
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            dp[i][1] = 1
            dp[i][0] = 0
            
        for j in range(1, n+1):
            dp[1][j] = j
            
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = sys.maxint
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1+max(dp[i-1][k-1], dp[i][j-k]))
        
        return dp[m][n]

