#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        
        i = m-1
        j = n-1
        ret = ""
        
        while i >= 0 and j >= 0:
            val = ord(A[i]) + ord(B[j]) - 2*ord('0')
            #print val
            ret = str(val) + ret
            
            i -= 1
            j -= 1
            
        if i >= 0:
            ret = A[:i+1] + ret
        if j >= 0:
            ret = B[:j+1] + ret
            
        return ret
        
