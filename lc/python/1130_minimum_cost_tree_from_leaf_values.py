#!/usr/bin/python -t

# state: dp[i][j] the minimum sum val from i to j.
# function: dp[i][j] = min(ret, dp[i][k] + dp[k+1][j]+max(arr[:k+1], arr[k:]))
# init: dp[i][j] = maxint
# result: ret

import sys
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[sys.maxint] * (n) for i in range(n)]
        m = [[0] * (n) for i in range(n)]

        for i in range(n):
            m[i][i] = arr[i]
            dp[i][i] = 0
            for j in range(i+1, n):
                m[i][j] = max(m[i][j-1], arr[j])

        #print dp, m
        
        for s in range(2, n+1):
            for i in range(n-s+1):
                j = s+i-1
                for k in range(i, j):
                    #m[i][j] = max(m[i][k], m[k+1][j])
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+m[i][k]*m[k+1][j])
                        
        #print dp
        return dp[0][n-1]

if __name__ == '__main__':
    s = [6,2,4]
    #s = [4, 11]
    #s = [11,12,12]
    ss = Solution()
    print('answer is %r' % ss.mctFromLeafValues(s))
