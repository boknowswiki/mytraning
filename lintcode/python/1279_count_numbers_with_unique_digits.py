#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

class Solution:
    """
    @param n: a non-negative integer
    @return: number of numbers with unique digits
    """
    def countNumbersWithUniqueDigits(self, n):
        # Write your code here
        # 设dp[i]表示i位数时满足题意的数的个数。
        # 对于第i位，为了使得第i位与前i-1位的数字不一致，我们可以选择数字应该有10-(i-1),
        # dp[i] = dp[i-1] * (11-i)
        # ret = sum(dp[i])
        
        if n == 0:
            return 1
            
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 9
        
        ret = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1] * (11-i)
            ret += dp[i]
            
        return ret

