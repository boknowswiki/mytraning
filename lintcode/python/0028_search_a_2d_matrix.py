#!/usr/bin/python -t

# binary search one search

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        # lower_bound for row and col
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
            
        l = 0
        r = m*n - 1
        
        while l < r:
            mid = (l+r)/2
            row = mid/(n)
            col = mid%(n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid
                
        if matrix[l/n][l%n] == target:
            return True
        return False

# binary search solution, search twice

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        # lower_bound for row and col
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
            
        l = 0
        r = m-1
        
        # find row first    
        while l < r:
            mid = (l+r)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                r = mid
        if matrix[l][0] == target:
            return True
       
        if matrix[l-1][0] < target <= matrix[l-1][n-1]: 
            row = l-1
        elif matrix[l][0] < target <= matrix[l][n-1]:
            row= l
        else:
            return False 
        # find col
        l = 0
        r = n-1
        
        while l < r:
            mid = (l+r)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
                
        if matrix[row][l] == target:
            return True
        return False

