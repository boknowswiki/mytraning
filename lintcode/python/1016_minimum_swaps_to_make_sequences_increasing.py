#!/usr/bin/python -t

# dp solution, zhuangtai dp, time O(n) space O(n)

class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # Write your code here
        # dp[i][0] the minimum number of swaps [0, i], when no swaps at ith place
        # dp[i][1] the minimum number of swaps [0, i], when swaps at ith place
        # 1. A[i] > A[i - 1] && B[i] > B[i - 1]
        # 2. A[i] > B[i - 1] && B[i] > A[i - 1]
        # 当 1 成立时: dp[i][0] = min(dp[i - 1][0], dp[i][0]), dp[i][1] = min(dp[i - 1] + 1, dp[i][1])

        # 当 2 成立时: dp[i][0] = min(dp[i][0], dp[i - 1][1]), dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
        # 边界: 除 dp[0][0] = 0, dp[0][1] = 1 之外, 其他状态初始值均为 INF.
        
        n = len(A)
        if n == 0:
            return 0
        
        keep = [sys.maxint] * (n)
        swap = [sys.maxint] * (n)
        
        keep[0] = 0
        swap[0] = 1
        
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                # no swap at i, so keep[i] = keep[i-1]
                keep[i] = keep[i-1]
                # swap at i, and i-1, then swap[i] = swap[i-1]+1
                swap[i] = swap[i-1]+1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                # no swap i, but swap at i-1
                keep[i] = min(keep[i], swap[i-1])
                # swap at i, no swap at i-1
                swap[i] = min(keep[i-1]+1, swap[i])
                
        return min(keep[n-1], swap[n-1])

