#!/usr/bin/python -t

# dp solution time O(m*n) space O(m*n)

# state: dp[i][j]: the longest common subsequence for first i from string 1, and first j from string 2
# function: if s1[i-1] == s2[j-1]:
#               dp[i][j] = dp[i-1][j-1]+1
#           else:
#               dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# init: dp[i][0] = dp[0][j] = 0
# result: dp[m][n]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for i in range(m+1)]
          
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]

