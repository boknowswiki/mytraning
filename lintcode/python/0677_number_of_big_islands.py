#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        # Write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if self.bfs(grid, i, j) >= k:
                        ret += 1
                        
        return ret
        
    def bfs(self, grid, x, y):
        q = deque()
        q.append((x,y))
        grid[x][y] = 0
        
        m = len(grid)
        n = len(grid[0])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        cnt = 0
        
        while len(q) > 0:
            cnt += 1
            cx, cy = q.popleft()
                
            for j in range(4):
                nx = cx + dx[j]
                ny = cy + dy[j]
                    
                if 0<= nx < m and 0<= ny < n and grid[nx][ny]:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
                        
        return cnt
        
        
# dfs


class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        # Write your code here
        m = len(grid)
        n = len(grid[0])
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and self.dfs(i, j, grid, k) >= k:
                    ret += 1
                    
        return ret
        
    def dfs(self, x, y, grid, k):
        ret = 1
        m = len(grid)
        n = len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        grid[x][y] = 0
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                ret += self.dfs(nx, ny, grid, k)
                
        return ret
        
            
