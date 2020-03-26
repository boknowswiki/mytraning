#!/usr/bin/python -t

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(t)
        n = len(s)
        if n == 0:
            return True
        if m == 0 or n > m:
            return False
        
        dp = [[False]*(n+1) for i in range(m+1)]
            
        for i in range(m+1):
            dp[i][0] = True
        
        print dp

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] or ((t[i-1] == s[j-1]) and dp[i-1][j-1])
                    
        print dp
        return dp[m][n]

if __name__ =='__main__':
    s = "abc"
    t = "ahbgdc"
    ss = Solution()
    print('answer is %r' % ss.isSubsequence(s, t))

