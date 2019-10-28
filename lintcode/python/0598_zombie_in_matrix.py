#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    
        days = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while len(q) > 0:
            l = len(q)
            days += 1
            
            for i in range(l):
                cx, cy = q.popleft()
                
                for j in range(4):
                    nx = cx + dx[j]
                    ny = cy + dy[j]
                    #print nx, ny
                    if 0<=nx < m and 0<= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
        
        #print grid                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
                    
        return days-1
        
        
