#!/usr/bin/python -t


import sys
from collections import deque

class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
            
        m = len(grid)
        n = len(grid[0])
        ret = sys.maxint
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ret = min(ret, self.bfs(grid, i, j))
                
        return ret if ret != sys.maxint else -1
        
    def bfs(self, grid, x, y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(grid)
        n = len(grid[0])
        
        v = set()
        q = deque()
        q.append((x, y))
        v.add((x, y))
        t = 0
        
        dist = 0
        while q:
            l = len(q)
            dist += 1
            for _ in range(l):
                cx, cy = q.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v:
                        v.add((nx, ny))
                        if grid[nx][ny] == 1:
                            t += dist
                        if grid[nx][ny] == 0:
                            q.append((nx, ny))
                            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in v:
                    return sys.maxint
                    
        return t
