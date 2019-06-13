#!/usr/bin/python -t

#区间 DP

#bottom up

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for lo in range (n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi))
                
        return dp[1][n]


#top down with memorization

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(lo, hi):
            if lo >= hi:
                return 0
            if lo + 1 == hi:
                return lo
            
            if self.dp[lo][hi] is None:
                self.dp[lo][hi] = min(i + max(dfs(lo, i-1), dfs(i+1, hi))
                                      for i in range(lo, hi+1))
            return self.dp[lo][hi]
        
        self.dp = [[None] * (n+1) for _ in range(n+1)]
        
        return dfs(1, n)
