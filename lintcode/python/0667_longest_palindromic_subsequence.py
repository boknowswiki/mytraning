#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

#对于任意字符串，如果头尾字符相同，那么字符串的最长子序列等于去掉首尾的字符串的最长子序列加上首尾；如果首尾字符不同，则最长子序列等于去掉头的字符串的最长子序列和去掉尾的字符串的最长子序列的较大者。
#
#设dp[i][j]表示第i到第j个字符间的最长回文序列的长度（i<=j）
#
#状态转移方程：
#
#dp[i][j]=dp[i+1][j-1] + 2\qquad if(str[i]==str[j])dp[i][j]=dp[i+1][j−1]+2if(str[i]==str[j])
#
#dp[i][j]=max(dp[i+1][j],dp[i][j-1])\quad if(str[i]!=str[j])dp[i][j]=max(dp[i+1][j],dp[i][j−1])if(str[i]!=str[j])


class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        # dp[i][j] the longest palindromic subsequence's lenght in [i, j]
        # dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1]+2)
        # dp[i][i] = 1 dp[i][i+1] = 1 if s[i] != s[i+1] else 2
        # dp[0][n-1]
        
        n = len(s)
        if n <= 1:
            return n
            
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l+i-1
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1]+2)
                    
        return dp[0][n-1]

