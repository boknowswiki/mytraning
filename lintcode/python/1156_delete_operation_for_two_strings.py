#!/usr/bin/python -t

class Solution:
    """
    @param word1: a string
    @param word2: a string
    @return: return a integer
    """
    def minDistance(self, word1, word2):
        # write your code here
        # dp[i][j] the minimum of steps for word1 at i to be the same as word2 at j
        # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]
        # else dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        # dp[i][0] = i, dp[0][j] = j
        # dp[m][n]
        
        m = len(word1)
        n = len(word2)
        
        print m,n
        dp = [[0] *(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            dp[i][0] = i
            
        print dp
        for j in range(1, n+1):
            dp[0][j] = j
            
        for i in range (1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                    
        return dp[m][n]

if __name__ == '__main__':
    s = "sea"
    d = "eat"
    ss = Solution()
    print "answer is %d" % ss.minDistance(s, d)
