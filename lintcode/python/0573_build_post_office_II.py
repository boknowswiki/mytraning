#!/usr/bin/python -t

# bfs AC answer:


import sys
from collections import deque

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxint for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxint
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
  
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)])
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1

# bfs Exceed time limit


import sys
from collections import deque

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
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
