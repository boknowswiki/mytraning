#!/usr/bin/python -t

#dp solution
# state dp[i][j] is s at i, t at j, how many solutions
# function dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# init dp[i][0] = 1, dp[0][j] = 0, j > 0
# result dp[m][n]
import pprint

    "", r, a, b, b, i ,t
["" [1, 0, 0, 0, 0, 0, 0],
 r  [1, 0, 0, 0, 0, 0, 0],
 a  [1, 0, 0, 0, 0, 0, 0],
 b  [1, 0, 0, 0, 0, 0, 0],
 b  [1, 0, 0, 0, 0, 0, 0],
 b  [1, 0, 0, 0, 0, 0, 0],
 i  [1, 0, 0, 0, 0, 0, 0],
 t  [1, 0, 0, 0, 0, 0, 0]]
["" [1, 0, 0, 0, 0, 0, 0],
 r  [1, 1, 0, 0, 0, 0, 0],
 a  [1, 1, 1, 0, 0, 0, 0],
 b  [1, 1, 1, 1, 0, 0, 0],
 b  [1, 1, 1, 2, 1, 0, 0],
 b  [1, 1, 1, 3, 3, 0, 0],
 i  [1, 1, 1, 3, 3, 3, 0],
 t  [1, 1, 1, 3, 3, 3, 3]]

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        pp = pprint.PrettyPrinter(indent=4)
        
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
            
        for j in range(1, n+1):
            dp[0][j] = 0
            
        pp.pprint(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        pp.pprint(dp)
        return dp[m][n]

if __name__ =='__main__':
    s = "rabbbit"
    t = "rabbit"
    ss = Solution()
    print('answer is')
    print ss.numDistinct(s, t)
