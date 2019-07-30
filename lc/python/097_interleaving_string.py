#!/usr/bin/python -t

#Here is some explanation:
#
#DP table represents if s3 is interleaving at (i+j)th position when s1 is at ith position, and s2 is at jth position. 0th position means empty string.
#
#So if both s1 and s2 is currently empty, s3 is empty too, and it is considered interleaving. If only s1 is empty, then if previous s2 position is interleaving and current s2 position char is equal to s3 current position char, it is considered interleaving. similar idea applies to when s2 is empty. when both s1 and s2 is not empty, then if we arrive i, j from i-1, j, then if i-1,j is already interleaving and i and current s3 position equal, it s interleaving. If we arrive i,j from i, j-1, then if i, j-1 is already interleaving and j and current s3 position equal. it is interleaving.

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
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                                (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                    
        return dp[m][n]

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

