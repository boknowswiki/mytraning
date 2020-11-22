#!/usr/bin/python -t

class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return True
            
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                    
        return True
        
                
