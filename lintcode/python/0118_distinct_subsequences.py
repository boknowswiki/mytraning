#!/usr/bin/python -t

# dp solution time O(n^2) space O(n^2)

class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        # write your code here
        # state: dp[i][j] the count of first j in T equals first i in S
        # function: dp[i][j] = dp[i-1][j-1],when T[j-1] == S[i-1] + dp[i-1][j]
        # init: dp[i][0] = 1, when T is empty, dp[0][j] = 0, when S is empty
        # result: dp[m][n]
        
        m = len(S)
        n = len(T)
            
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        #for j in range(n+1):
        #    dp[0][j] = 0

        print dp
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if T[j-1:j] == S[i-1:i]:
                    dp[i][j] = dp[i-1][j-1] 
                dp[i][j] += dp[i-1][j]

        return dp[m][n]

if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    ss = Solution()
    print "answer is %s" % ss.numDistinct(s, t)
