#!/usr/bin/python -t

#DP my own solution beat 100%
#time O(n2), space O(n)

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return False
            
        if n == 1:
            return True
        dp = [0] * n
        
        dp[0] = A[0]
        
        for i in range(n-1):
            if dp[i] != 0:
                for j in range(A[i]):
                    if i+j > n-1:
                        return True
                    dp[i+j] = 1           
            else:
                return False
                    
        return True

