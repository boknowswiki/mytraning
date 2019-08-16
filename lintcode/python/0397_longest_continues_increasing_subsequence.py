#!/usr/bin/python -t

# dp solution time O(n), space O(n)

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        # state: dp[i] the longest increasing number at i
        # function: dp[i] = dp[i-1] + 1, if A[i] > A[i-1]
        # init:dp[i] = 1
        # result: dp[n-1]
        # try consistent space solution
        
        n = len(A)
        if n == 0:
            return 0
        ret = 1
        
        dp = [1] * n
        
        for i in range(1, n):
            if A[i] > A[i-1]:
                dp[i] = dp[i-1] + 1

            ret = max(ret, dp[i])
            
        dp = [1] * n
        
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                dp[i] = dp[i+1] + 1

                
            ret = max(ret, dp[i])
            
        return ret

# dp, time O(n) space O(1)

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        # state: dp[i] the longest increasing number at i
        # function: dp[i] = dp[i-1] + 1, if A[i] > A[i-1]
        # init:dp[i] = 1
        # result: dp[n-1]
        # try consistent space solution
        
        n = len(A)
        if n == 0:
            return 0
        inc = 1
        dec = 1
        ret = 1
            
        for i in range(1, n):
            if A[i] > A[i-1]:
                inc += 1
                dec = 1
            else:
                inc = 1
                dec += 1
                
            ret = max(ret, inc, dec)
            
        return ret

