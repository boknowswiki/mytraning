#!/usr/bin/python -t

# binary search
# 从左下角开始，往右上角逼近

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
            
        cnt = 0
        
        row = m-1
        col = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                cnt += 1
                col += 1
                row -= 1
                
        return cnt
        
