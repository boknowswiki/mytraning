#!/usr/bin/phthon -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        # state: dp[i] is the first player can win
        # function: dp[i] = dp[i-1] == False or dp[i-2] == False, only the previous two lose, the thrid step can win
        # init: dp[0] = False, dp[1] = True, dp[2] = True
        # result: dp[n]
        
        # n+3 to cover n = 0, 1, 2 cases
        dp = [False] * (n+3)
        dp[0] = False
        dp[1] = True
        dp[2] = True
        if n <= 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp[i] = (dp[i-1] == False) or (dp[i-2] == False)
            
        return dp[n]

