#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        # write your code here
        # state: dp[i] is the minimum cuts for the first ith substring is palindrome
        # function: dp[i] = min(dp[j]+1, dp[i]) for j in [0,i] and s[j:i+1] is palindrome
        # init: dp[i] = 0
        # result: dp[i] which dp[i] != 0 and i from [n,0]
        #可以看作序列型动态规划问题, 设定 dp[i] 表示原串的前 i 个字符最少分割多少次可以使得到的都是回文子串.
        #
        #如果 s 前 i 个字符组成的子串本身就是回文串, 则 dp[i] = 0, 否则:
        #
        #dp[i] = min{dp[j] + 1} (j < i 并且 s[j + 1], s[j + 2], ... , s[i] 是回文串)
        #如果想要是 O(n^2) 的时间复杂度 (n 是 s 的长度), 需要事先求出来回文串信息, 在状态转移时可以 O(1) 地知道一段子串是否回文的.
        
        n = len(s)
        
        dp = [sys.maxint] * (n+1)
        dp[0] = 0
        palindrome = [[False] * (n) for i in range(n)]
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if i == j:
                    palindrome[i][j] = True
                elif i+1 == j:
                    palindrome[i][j] = True if s[i] == s[j] else False
                else:
                    palindrome[i][j] = True if s[i] == s[j] and palindrome[i+1][j-1] else False
                    
        for i in range(1, n+1):
            for j in range(i):
                if palindrome[j][i-1]:
                    dp[i] = min(dp[i], dp[j]+1)
                    
        return dp[n] - 1

