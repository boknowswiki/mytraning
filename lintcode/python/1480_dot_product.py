#!/usr/bin/python -t


class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        if len(A) == 0 or len(B) == 0 or len(A) != len(B):
            return -1
        ans = 0
        n = len(A)
        for i in range(n):
            ans += A[i] * B[i]
        return ans
