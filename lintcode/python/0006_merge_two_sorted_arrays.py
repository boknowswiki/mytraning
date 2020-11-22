#!/usr/bin/python -t

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        p1, p2 = 0, 0
        result = []
        while p1!=len(A) and p2!=len(B):
            if A[p1] <= B[p2]:
                result.append(A[p1])
                p1 = p1 +1
            else:
                result.append(B[p2])
                p2 = p2 +1
        
        if p1==len(A):
            result = result + B[p2:]
        if p2 == len(B):
            result = result + A[p1:]
        
        return result
