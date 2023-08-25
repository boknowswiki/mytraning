#!/usr/bin/python -t

# dp

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = true indicates at ith in s1, jth in s2 can concatenation to s3[i+j] otherwise false
        # dp[i][j] = if dp[i-1][j] == true and s1[i] == s3[i+j] or dp[i][j-1] == true and s2[j] == s3[i+j]
        # dp[0][0] = true
        # return dp[n][m]
        
        n, m = len(s1), len(s2)
        if len(s3) != m+n:
            return False

        if m > n:
            return self.isInterleave(s2, s1, s3)

        dp = [[False] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1+j]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[n][m]

# dfs with memo
 public class Solution {
    public boolean is_Interleave(String s1, int i, String s2, int j, String s3, int k, int[][] memo) {
        if (i == s1.length()) {
            return s2.substring(j).equals(s3.substring(k));
        }
        if (j == s2.length()) {
            return s1.substring(i).equals(s3.substring(k));
        }
        if (memo[i][j] >= 0) {
            return memo[i][j] == 1 ? true : false;
        }
        boolean ans = false;
        if (s3.charAt(k) == s1.charAt(i) && is_Interleave(s1, i + 1, s2, j, s3, k + 1, memo)
                || s3.charAt(k) == s2.charAt(j) && is_Interleave(s1, i, s2, j + 1, s3, k + 1, memo)) {
            ans = true;
        }
        memo[i][j] = ans ? 1 : 0;
        return ans;
    }
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        int memo[][] = new int[s1.length()][s2.length()];
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                memo[i][j] = -1;
            }
        }
        return is_Interleave(s1, 0, s2, 0, s3, 0, memo);
    }
}

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

