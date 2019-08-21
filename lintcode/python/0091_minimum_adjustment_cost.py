#!/usr/bin/python -t

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        # state: dp[i][k] the minimize sum of when i becomes k
        #        dp[i-1][j] is the minimize sum of when i-1, j becomes k
        # function: dp[i][k] = min(dp[i][k], dp[i-1][j] + abs(A[i-1]-k)
        # init: dp[i][k] = sys.maxint, dp[0][k] = 0
        # result: min(dp[n][k])
        #1.DP[i][k] 表示当我们走到A[i-1]、并且把A[i-1]这个数变成k，所需要的最小步数是多少；
        #2.首先，DP[0][k] 都是0，因为没有数就代表不需要移步它；
        #3.然后，每走到一个 DP[i][k]，我们可以知道，在它之前的移步是有限制的，是 DP[i-1][j] 并且 abs(j-k) <= target 才能让 DP[i][k] 走到这一步。因此，DP[i][k] = min(DP[i][k], DP[i-1][j] + abs(A[i-1]-k)) 这个式子就是这么来的。
        #4.最后，我们要遍历 DP[A.size()][0-100]，因为我们要看看最后一个数分别变成 0，1，2...100 后谁的总移步数最小，就选谁。
        
        n = len(A)
        dp = [[sys.maxint] * (101) for i in range(n+1)]
        for i in range(101):
            dp[0][i] = 0
            
        for i in range(1, n+1):
            for j in range(101):
                if dp[i-1][j] != sys.maxint:
                    for k in range(101):
                        if abs(j-k) <= target:
                            dp[i][k] = min(dp[i][k], dp[i-1][j] + abs(A[i-1]-k))
                            
        ret = sys.maxint
        for i in range(101):
            ret = min(ret, dp[n][i])
            
        return ret

