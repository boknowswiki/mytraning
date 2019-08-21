#!/usr/bin/python -t 

# dp solution, time O(mn) space O(mn)

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        # state: dp[i][j] is in s3 or not
        # function: dp[i][j] = true if (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] an dp[i][j-1])
        # init: dp[0][0] = true
        # result: dp[m][n]
        
        m = len(s1)
        n = len(s2)
        k = len(s3)
        if k != m+n:
            return False
            
        dp= [[False] * (n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if i == 0:
                    if s2[j-1] == s3[j-1] and dp[0][j-1]:
                        dp[i][j] = True
                    continue
                if j == 0:
                    if s1[i-1] == s3[i-1] and dp[i-1][0]:
                        dp[i][j] = True
                    continue
                if (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1]):
                    dp[i][j] = True
                    
        return dp[m][n]

