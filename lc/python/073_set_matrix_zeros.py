#!/usr/bin/python -t

# hash map
# time O(mn)
# space O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])

        r_set = set()
        c_set = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r_set.add(i)
                    c_set.add(j)

        for i in range(m):
            for j in range(n):
                if i in r_set or j in c_set:
                    matrix[i][j] = 0

        return

#time O(mn) space O(1)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        is_col = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
                
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
                    
        return
