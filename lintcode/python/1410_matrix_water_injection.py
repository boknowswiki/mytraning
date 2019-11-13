#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here
        m = len(matrix)
        n = len(matrix[0])
        
        return "YES" if self.dfs(R, C, m, n, matrix) else "NO"
        
    def dfs(self, x, y, m, n, matrix):
        if x == 0 or y == 0 or x == m-1 or y == n-1:
            return True
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            
            if 0<=nx<m and 0<=ny<n and matrix[x][y] > matrix[nx][ny]:
                if self.dfs(nx, ny, m, n, matrix):
                    return True
                
        return False
        
