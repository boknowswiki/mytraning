#!/usr/bin/python -t

#dp solution

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        
        max_len = 0
        
        for i in range(m):
            for j in range(n):
                length = 0
                while i+length < m and j+length < n and A[i+length] == B[j+length]:
                    length = length + 1
                    if length > max_len:
                        max_len = length
                        
        return max_len

