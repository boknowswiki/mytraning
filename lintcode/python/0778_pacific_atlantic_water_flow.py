#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []
            
        #ret = []
        p, a = set(), set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            self.dfs(i, 0, matrix, p, 0)
            self.dfs(i, n-1, matrix, a, 0)
            
        for i in range(n):
            self.dfs(0, i, matrix, p, 0)
            self.dfs(m-1, i, matrix, a, 0)
            
        ret = list(p&a)
        
        return ret
        
    def dfs(self, x, y, matrix, v, h):
        if matrix[x][y] < h:
            return
        
        m = len(matrix)
        n = len(matrix[0])
        v.add((x, y))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<m and 0<=ny<n and (nx, ny) not in v:
                self.dfs(nx, ny, matrix, v, matrix[x][y])
                
        return
    
