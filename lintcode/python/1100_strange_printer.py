#!/usr/bin/python -t

#区间dp
#题解：
#dp[i][j]表示区间(i,j)的最优解，temp = dp[j][k - 1] + dp[k][j + i] 实现小区间合并大区间更新答案，合并时需要判断两区间尾部。如果相同，需要减一即可。

class Solution:
    """
    @param s: 
    @return: the minimum number of turns the printer needed in order to print it
    """
    def strangePrinter(self, s):
        # write your code here
        s = '#' + s
        s = ''.join([s[i] for i in range(1, len(s)) if s[i] != s[i-1]])
        #print s
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                #print i, j
                ans = dp(i+1, j) + 1
                #print "i, j, ans:", i,j, ans
                for k in range(i+1, j+1):
                    #print k, i, s[k], s[i]
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                        #print ans, i, k, j
                memo[i, j] = ans
                #print i, j, ans
            return memo[i, j]
    
        return dp(0, len(s) - 1)
