#!/usr/bin/python -t

# dp solution time O(n^2) space O(n)

class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # state: dp[i] is the least number of perfect square numbers which sum to i
        # function: dp[i] = min(dp[i], dp[i-j^2]+1), 0<j*j <=i
        # init: dp[0] = 0, dp[1] = 1
        # result: dp[n]
        
        dp = [sys.maxint] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)

        return dp[n]

if __name__ == '__main__':
    s = 12
    ss = Solution()
    print "answer is %s" % ss.numSquares(s)
