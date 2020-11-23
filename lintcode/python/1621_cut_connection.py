#!/usr/bin/python -t

class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """
    def removeOne(self, matrix, x, y):
        # Write your code here
        while x < len(matrix):
            if(int(matrix[x][y])== 1):
                matrix[x][y] = 0
            x += 1
        return matrix
