#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        # write your code here
        m = len(A)
        n = len(B)
        max_sum = -sys.maxint
        ret = []
        
        l = 0
        r = n-1
        
        while l < m and r >= 0:
            while l > 0 and A[l] == A[l-1]:
                l += 1
            while r > 0 and B[r] == B[r-1]:
                r -= 1
                
            val = A[l] + B[r]
            if val == K:
                return [l, r]
            elif val > K:
                r -= 1
            else:
                if val > max_sum:
                    max_sum = val
                    ret = [l, r]
                l += 1
                    
        return ret
        
