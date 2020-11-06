#!/usr/bin/python -t

# dfs + mem

class Solution:
    """
    @param matrix: 
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return 0
            
        m = len(matrix)
        n = len(matrix[0])
        
        self.ret = sys.maxint
        
        mem = [[sys.maxint] * n for _ in range(m)]
        
        for j in range(n):
            mem[0][j] = matrix[0][j]
        
        for j in range(n):
            self.dfs(matrix, m, n, 0, j, matrix[0][j], mem)
            
        return self.ret
        
    def dfs(self, matrix, m, n, x, y, t, mem):
        if x == m-1:
            self.ret = min(self.ret, t)
            
        if t > mem[x][y]:
            return
        
        mem[x][y] = t
            
        dx = [1, 1, 1]
        dy = [-1, 0, 1]
        
        for i in range(3):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < m and 0 <= cy < n:
                self.dfs(matrix, m, n, cx, cy, t+matrix[cx][cy], mem)
                
        return
