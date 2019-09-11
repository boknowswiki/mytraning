#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        # Write your code here
        # dp[i] the minimum steps for n 'A'
        # dp[i] = dp[j] + (i/j) if i%j == 0
        # dp[n]
        
        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            #worse case or maximum case will be paste 'A' one by one
            dp[i] = i
            for j in range(i-1, 1, -1):
                # if i is multiple of j, then paste based on dp[j] will save more steps
                if i%j == 0:
                    dp[i] = dp[j] + (i/j)
                    break
                    
        return dp[n]

