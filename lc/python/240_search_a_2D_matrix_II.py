#!/usr/bin/python -t

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col = col + 1
            else:
                row = row - 1
                
        return False
