#!/usr/bin/python -t

# dp solution, time O(n) space O(1)

class Solution:
    """
    @param n: the number of sectors
    @param m: the number of colors
    @return: The total number of plans.
    """
    def getCount(self, n, m):
        # Write your code here
        # dp[i] is the numbers of plans at sector i
        # f[1] = m, f[2] = m*(m-1), f[3] = m*(m-1)*(m-2) 
        # when i>=4, f[4] = f[i-1]*(m-2) + f[i-2]*(m-1)
        # ret = f[n]
        
        MOD = 1000000007
        if n == 1:
            return m
        if n == 2:
            return m*(m-1) % MOD
        if n == 3:
            return m*(m-1)*(m-2) % MOD
        
        f1 = m*(m-1) % MOD
        f2 = m*(m-1)*(m-2) % MOD
        for i in range(4, n+1):
            tmp = f2
            f2 = (f2*(m-2) + f1*(m-1)) % MOD
            f1 = tmp
            
        return f2

