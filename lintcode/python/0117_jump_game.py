#!/usr/bin/python

#dp solution

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        n = len(A)

        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            dp[i] = sys.maxint
            for j in range(i):
                if dp[j] != sys.maxint and A[j]+j >= i:
                    dp[i] = dp[j] + 1
                    break
        
        return dp[n-1]

