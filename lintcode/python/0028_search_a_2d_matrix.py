#!/usr/bin/python3 -t

# binary search
# time O(log(m) + log(n))
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        row = self.find_row(matrix, target)

        return self.find_num(matrix[row], target)

    def find_row(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        if target >= matrix[m-1][0]:
            return m-1
        start = 0
        end = m-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid

        if target > matrix[end][0]:
            return end
        return start

    def find_num(self, row, target):
        start = 0
        end = len(row)-1

        while start + 1 < end:
            mid = start + (end-start)//2
            if row[mid] > target:
                end = mid
            else:
                start = mid

        if row[end] == target:
            return True
        if row[start] == target:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
    a = [[1,4,5],[6,7,8]]
    b = 3
    print(s.search_matrix(a, b))

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

