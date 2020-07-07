#!/usr/bin/python -t

# 正确的算法请参考: http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf

# time O(m+n)

class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        m, n = len(A), len(A[0])
        return self.find(A, 0, m-1, 0, n-1)
        
    def find(self, A, top, bottom, left, right):
        row_mid = (top+bottom)/2
        col_mid = (left+right)/2
        max_num = A[row_mid][col_mid]
        row, col = row_mid, col_mid
        
        # find max_num in row
        for i in range(top, bottom+1):
            if A[i][col_mid] > max_num:
                max_num = A[i][col_mid]
                row = i
                col = col_mid
                
        # find max_num in col
        for j in range(left, right+1):
            if A[row_mid][j] > max_num:
                max_num = A[row_mid][j]
                col = j
                row = row_mid
                
        if row -1 >= 0 and A[row-1][col] > A[row][col]:
            row -= 1
        elif row+1 < len(A) and A[row+1][col] > A[row][col]:
            row += 1
        elif col - 1 >= 0 and A[row][col-1] > A[row][col]:
            col -= 1
        elif col + 1 < len(A[0]) and A[row][col+1] > A[row][col]:
            col += 1
        else:
            return [row, col]

        
        if (row >= top and row < row_mid and col >= left and col < col_mid):
            return self.find(A, top, row_mid - 1, left, col_mid - 1)
        elif (row >= top and row < row_mid and col >= col_mid and col <= right):
            return self.find(A, top, row_mid - 1, col_mid + 1, right)
        elif (row > row_mid and row <= bottom and col >= left and col < col_mid):
            return self.find(A, row_mid + 1, bottom, left, col_mid - 1)
        elif (row > row_mid and row <= bottom and col > col_mid and col <= right):
            return self.find(A, row_mid + 1, bottom, col_mid + 1, right)
        
        return [-1, -1]