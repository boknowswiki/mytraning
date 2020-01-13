#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        # write your code here
        A.sort()
        B.sort()
        m = len(A)
        n = len(B)
        ret = sys.maxint
        
        i = 0
        j = 0
        
        while i < m and j < n:
            diff = A[i] - B[j]
            ret = min(ret, abs(diff))
            if diff == 0:
                return ret
            elif diff > 0:
                j += 1
            else:
                i += 1
                
        while i < m:
            ret = min(ret, abs(A[i] - B[j-1]))
            i += 1
        while j < n:
            ret = min(ret, abs(A[i-1] - B[j]))
            j += 1
            
        return ret
        
