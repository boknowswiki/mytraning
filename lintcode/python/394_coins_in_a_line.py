#!/usr/bin/python -t

# dp solution

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n < 3:
            return n > 0
            
        dp = [False] * (n+1)
        
        dp[0] = False
        dp[1] = True
        dp[2] = True
        
        for i in range(3, n+1):
            dp[i] = (not dp[i-1]) or (not dp[i-2])
            
        return dp[n]

import sys

sys.setrecursionlimit(1500)

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n < 3:
            return n > 0
            
        dp = [False] * (n+1)
        v = [False] * (n+1)
        
        dp[n] = self.search(n, dp, v)
    
        return dp[n]
        
    def search(self, i, dp, v):
        if v[i]:
            return dp[i]
            
        if i < 3:
            dp[i] = True if i != 0 else False
            return dp[i]
            
        dp[i] = (not self.search(i-1, dp, v)) or (not self.search(i-2, dp, v))
        
        return dp[i]

if __name__ == '__main__':
    s= 1000
    ss = Solution()
    print "answer is %s" % ss.firstWillWin(s)
