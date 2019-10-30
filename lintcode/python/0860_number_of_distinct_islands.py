#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        shapes = set()
        
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = self.bfs(grid, i, j)
                    if shape in shapes:
                        continue
                    
                    cnt += 1
                    shapes.add(shape)
                    
        return cnt
        
    def bfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        shape = ''
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        q = deque()
        q.append((x,y))
        grid[x][y] = 0
        
        while len(q):
            cx, cy = q.popleft()
            shape += str(cx-x) + str(cy-y)
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    grid[nx][ny] = 0
                    
        return shape
        
    
