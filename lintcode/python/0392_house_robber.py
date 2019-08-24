#!/usr/bin/python -t

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
            
        f = [0] * 3
        f[0], f[1] = A[0], max(A[0], A[1])
        
        for i in range(2, len(A)):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + A[i])
            
        return f[(len(A) - 1) % 3]


# dp solutoin time O(n) space O(n)

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        # state: dp[i] the maximum money can rob at house i
        # function: dp[i] = max(dp[i-1], dp[i-2]+A[i-1])
        # init: dp[i] = 0
        # result: max(dp[n], dp[n-1])
        
        n = len(A)
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[1] = A[0]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+A[i-1])
        
        return dp[n]

