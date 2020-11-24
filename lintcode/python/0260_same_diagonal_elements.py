#!/usr/bin/python -t

class Solution:
    """
    @param matrix: a matrix
    @return: return true if same.
    """
    def judgeSame(self, matrix):
        # write your code here.
        if not matrix or not matrix[0]:
            return True
            
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m-1):
            for j in range(n-1):
                if i+1 < m and j +1 < n:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
                        
        return True
