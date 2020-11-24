#!/usr/bin/python -t

class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        # Write your code here.
        if not A:
            return False
            
        n = len(A)
        
        if n < 2:
            return True
            
        increase = A[1] >= A[0]
        
        for i in range(1, n):
            if increase:
                if A[i] < A[i-1]:
                    return False
                    
            else:
                if A[i] > A[i-1]:
                    return False
                    
        return True
