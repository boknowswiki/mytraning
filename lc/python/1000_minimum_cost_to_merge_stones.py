#!/usr/bin/python -t

import sys

# dp solution time O(n^3/K) space O(n^2)

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        
        if (n-1)%(K-1) > 0:
            return -1
        
        dp =[[0] * (n) for i in range(n)]
        val = [0] * (n+1)
        
        for i in range(n):
            val[i+1] = val[i] + stones[i]
        
        for k in range(K, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if j > n:
                    break
                dp[i][j] = sys.maxint
                for mid in range(i, j, K-1):
                    dp[i][j] = min(dp[i][j], dp[i][mid]+dp[mid+1][j])
                if (j-i)%(K-1) == 0:
                    dp[i][j] += val[j+1]-val[i]
                    
        return dp[0][n-1]

if __name__ == '__main__':
    s = [3,2,4,1]
    k = 2
    ss = Solution()
    print('answer is %r' % ss.mergeStones(s, k))
