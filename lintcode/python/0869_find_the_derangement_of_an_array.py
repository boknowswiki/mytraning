#!/usr/bin/python -t

class Solution:
    """
    @param n: an array consisting of n integers from 1 to n
    @return: the number of derangement it can generate
    """
    def findDerangement(self, n):
        # Write your code here
        # dp[i] the number of derangement at i place
        # dp[i] = (i-1)*(dp[i-1]+dp[i-2])
        # dp[1] = 0, dp[2] = 1
        # dp[n]
        
        if n <= 1:
             return 0
        
        x, y = 0, 1
        MOD = 10**9 + 7
        
        for i in range(3, n+1):
            x, y = y, (i-1)*(x+y)%MOD
        #print x, y    
        return y

# dp solution, MLE, time O(n) space O(n)

class Solution:
    """
    @param n: an array consisting of n integers from 1 to n
    @return: the number of derangement it can generate
    """
    def findDerangement(self, n):
        # Write your code here
        # dp[i] the number of derangement at i place
        # dp[i] = (i-1)*(dp[i-1]+dp[i-2])
        # dp[1] = 0, dp[2] = 1
        # dp[n]
        
        if n <= 1:
             return 0
        
        dp = [0] * (n+1)
        dp[2] = 1
        MOD = 10**9 + 7
        
        for i in range(3, n+1):
            dp[i] = (i-1) * (dp[i-1]+dp[i-2])%MOD
            
        return dp[n]

if __name__ == '__main__':
    s = 1000000
    ss = Solution()
    print "answer is %s" % ss.findDerangement(s)
