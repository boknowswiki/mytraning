#!/usr/bin/python -t

#区间动态规划.
#
#设定状态: f[i][j] 表示合并原序列 [i, j] 的石子的最小分数
#
#状态转移: f[i][j] = min{f[i][k] + f[k+1][j]} + sum[i][j], sum[i][j] 表示原序列[i, j]区间的重量和
#
#边界: f[i][i] = sum[i][i], f[i][i+1] = sum[i][i+1]
#
#答案: f[0][n-1]

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0
            
        # dp[i][j] => minimum cost merge from i to j
        dp = [[0] * n for _ in range(n)]
        # range_sum[i][j] => A[i] + A[i + 1] ... + A[j]
        range_sum = self.get_range_sum(A)
            
        # enumerate the range size first, start point second
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for mid in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + range_sum[i][j])
        
        return dp[0][n - 1]
                    
    def get_range_sum(self, A):
        n = len(A)
        range_sum = [[0] * n for _ in range(len(A))]
        for i in range(n):
            range_sum[i][i] = A[i]
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j - 1] + A[j]
        return range_sum

# dp solution, time O(n^2) space O(n^2)

import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        # state: dp[i][j] is the minimum of score from i to j pile
        # function: dp[i][j] = min(dp[i][j, dp[i][k]+dp[k+1][j]+sum_val[j+1]-sum_val[i])
        # init: sum_val[i] is first ith piles sum
        # result: dp[0][n-1]
        
        n = len (A)
        if n == 0:
            return 0
        
        sum_val = [0] * (n+1)
        
        for i in range(1,n+1):
            sum_val[i] = sum_val[i-1] + A[i-1]
        print sum_val
            
        dp = [[0] * n for i in range(n)]
        
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                dp[i][j] = sys.maxint
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum_val[j+1]-sum_val[i])
                    
        return dp[0][n-1]

if __name__ == '__main__':
    s = [3,4,3]
    ss = Solution()
    print "answer is %s" % ss.stoneGame(s)
