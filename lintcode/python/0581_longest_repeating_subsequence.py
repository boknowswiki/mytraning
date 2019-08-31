#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class Solution:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longestRepeatingSubsequence(self, str):
        # write your code here
        # dp[i][j], maximum len of matching character for the first ith, and jth
        # dp[i][j] = max(dp[i-1][j-1]+1) if str[i] == str[j]
        
        n = len(str)
        
        dp = [[0] * (n+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(i, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if str[i-1] == str[j-1] and i != j:
                    dp[i][j] = dp[i-1][j-1]+1
                    
                
        return dp[n][n]


class Solution:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longestRepeatingSubsequence(self, str):
        # write your code here
        # dp[i][j], maximum len of matching character for the first ith, and jth
        # dp[i][j] = max(dp[i-1][j-1]+1) if str[i] == str[j]
        
        n = len(str)
        
        dp = [[0] * (n+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if str[i-1] == str[j-1] and i != j:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[n][n]

if __name__ == '__main__':
    s = "aab"
    ss = Solution()
    print "answer is %s" % ss.longestRepeatingSubsequence(s)

