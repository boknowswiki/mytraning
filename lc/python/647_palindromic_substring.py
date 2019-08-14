#!/usr/bin/python -t

# state: dp[i][j], from i to j, if it's palindromic then 1, else 0
# function: dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
# init: dp[i][i] = 1, for single character, it's palindromic. so 1
# result: for every dp[i][j] == 1, add them together for result

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for i in range(n)]
        ret = 0

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for d in range(1, n-i):
                j = i + d
                if d == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] else 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    ret = ret + 1

        return ret
            

if __name__ == '__main__':
    s = "abc"
    ss = Solution()
    print('answer is %r' % ss.countSubstrings(s))
