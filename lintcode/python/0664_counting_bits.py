#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        # dp[i] the number of 1 in number i
        # dp[i] = dp[i>>1] + i%2
        # or dp[i] = i % 2 == 1? dp[i/2] + 1: dp[i/2] 
        # dp[0] = 0
        
        dp = [0] * (num+1)
        dp[0] = 0

        for i in range(1, num+1):
            dp[i] = dp[i>>1]+i%2
            
        return dp

