#!/usr/bin/python -t

class Solution:
    """
    @param A: a matrix
    @return: the resulting image
    """
    def flipAndInvertImage(self, A):
        # Write your code here
        if not A or not A[0]:
            return A
            
        m = len(A)
        n = len(A[0])
        
        for i in range(m):
            self.reverse(A[i])
            
        for i in range(m):
            for j in range(n):
                A[i][j] ^= 1
                
        return A
            
            
            
    def reverse(self, a):
        l = 0
        r = len(a)-1
        
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
            
        return
