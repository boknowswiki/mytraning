#!/usr/bin/python -t

# dp solution time O(n^3) space O(nk)

class Solution:
    """
    @param A: an array
    @param K: an integer
    @return: the largest score
    """
    def largestSumOfAverages(self, A, K):
        # Write your code here

        #分k组 要求元素个数最少为k
        #对于已知所有的k - 1组的数据的情况下
        #dp[k][n] = Math.max(dp[k - 1][j] + average(j + 1, n))

        #dp[i][j]表示前i个数分成j段的最大和
        #为了方便我们计算，我们可以加上一个sum[i], sum[i]表示其前缀和
        # state: dp[i][j] means for i numbers to splite to j groups, the max sum.
        # function: dp[i][j] = max(dp[i][j], dp[i-1][t]+(sum[j]-sum[t])/(j-t)) j-1<t<i
        # init: dp[0][i] = 0, dp[1][i] = sum(A[:i])/i
        # result: dp[k][n]
        
        n = len(A)
        dp = [[0.0] * (n+1) for i in range(K+1)]
        sum_val = [0.0] * (n+1)
        
        for i in range(1, n+1):
            sum_val[i] = sum_val[i-1] + A[i-1]
            dp[1][i] = sum_val[i]/i
            
        for i in range(2, K+1):
            for j in range(i, n+1):
                for t in range(i-1, j):
                    dp[i][j] = max(dp[i][j], dp[i-1][t]+(sum_val[j]- sum_val[t])/(j-t))
                    
        return dp[K][n]

