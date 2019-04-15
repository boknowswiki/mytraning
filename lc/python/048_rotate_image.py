#!/usr/bin/python -t

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        
        for i in range(m):
            matrix[i] = matrix[i][::-1]
            
        for i in range(m-1):
            for j in range(i, m-1):
                matrix[i][m-2-j], matrix[j+1][m-1-i] = matrix[j+1][m-1-i], matrix[i][m-2-j]
                
        return
