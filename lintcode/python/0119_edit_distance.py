#!/usr/bin/python -t

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        # state: dp[i][j], minimum steps for word1 first ith equals words first jth
        # function: if word1[i-1] == word2[j-1] dp[i][j] = dp[i-1][j-1] else dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        # init: dp[i][0] = i dp[0][j] = j
        # result:dp[m][n]
        
        m = len(word1)
        n = len(word2)
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        print dp
                    
        return dp[m][n]

if __name__ == '__main__':
    s ="horse"
    d = "ros"
    ss = Solution()
    print "answer is %s" % ss.minDistance(s, d)

