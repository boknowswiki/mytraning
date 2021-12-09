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
        n = len(s)
        dp = [
          [float('inf')] * n
          for _ in range(n)
        ]

        for i in range(n):
          dp[i][i] = 1

        for size in range(2, n + 1):
          for i in range(n):
            j = i + size - 1
            if j >= n:
              break
            for k in range(i, j):
              temp = dp[i][k] + dp[k + 1][j]
              if s[k] == s[j]:
                temp -= 1
              dp[i][j] = min(dp[i][j], temp)
        return dp[0][n - 1]

class Solution:
    """
    @param s:
    @return: the minimum number of turns the printer needed in order to print it
    """
    def strangePrinter(self, s):
        # write your code here
        dp = [[0 for i in range(102)] for i in range(102)]
        n = len(s)
        if n == 0:
            return 0

        for i in range(n):
            dp[i][i] = 1

        for length in range(1, n):  #枚举区间长度
            for j in range(0, n-length):    #枚举起点
                dp[j][j+length] = length+1
                for k in range(j+1, j+length+1):
                    tmp = dp[j][k-1]+dp[k][j+length]    #小区间合并成为大区间，答案更新，判断尾部，相同减一
                    if s[k-1] == s[j+length]:
                        tmp -=1
                    dp[j][j+length] = min(dp[j][j+length], tmp)
        return dp[0][n-1]

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
