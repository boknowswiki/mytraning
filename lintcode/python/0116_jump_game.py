#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # state: dp[i], wether we can reach point i
        # function: dp[i] = true if dp[j] == true and A[j] >= i-j, 0<=j<i
        # init: dp[0] = true
        # result dp[n-1]
        
        n = len(A)
        dp = [False] * n
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i):
                if dp[j] and A[j] >= i-j:
                    dp[i] = True
                    break
                
        return dp[n-1]


#greedy O(n)

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
            
        far = A[0]
        
        for i in range(n):
            if i <= far and i+A[i] > far:
                far = i+A[i]
                
        return far >= n-1

#dp O(n2)

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        canjump = [False] * n
        canjump[0] = True
        
        for i in range(1, n):
            for j in range(0, i):
                if canjump[j] and j + A[j] >= i:
                    canjump[i] = True
                    break
                    
        return canjump[n-1]

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

