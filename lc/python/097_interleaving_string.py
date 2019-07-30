#!/usr/bin/python -t

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        k = len(s3)
        
        if k != m+n:
            return False
        
        dp = [[False]*(n+1) for i in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(1,m+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
                
        for j in range(1, n+1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
                    
        return dp[m][n]

