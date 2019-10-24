#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        v = set()
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and ((i, j) not in v):
                    ret += 1
                    self.bfs(grid, i, j, v)
                    
        return ret
        
    def bfs(self, grid, x, y, v):
        m = len(grid)
        n = len(grid[0])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        q = deque([(x, y)])
        v.add((x, y))
        
        while len(q) > 0:
            cx, cy = q.popleft()
            
            for i in range(4):
                nx, ny = cx+dx[i], cy + dy[i]
                
                if 0<=nx < m and 0<=ny < n and ((nx, ny) not in v) and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    v.add((nx, ny))
                    
        return


# union find set 
    

class uf:
    def __init__(self, grid):
        m = len(grid)
        self.cnt = 0
        if m == 0:
            return
        
        n = len(grid[0])
        if n == 0:
            return
        
        self.father = [0] * (m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.cnt += 1
                self.father[i*n+j] = i*n+j
        
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        self.father[proot] = qroot
        self.cnt -= 1
        
    def find(self, p):
        if p != self.father[p]:
            self.father[p] = self.find(self.father[p])
            
        return self.father[p]

    def query(self):
        return self.cnt

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        myuf = uf(grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                p = i*n+j
                if i > 0 and grid[i-1][j] == 1:
                    q = p-n
                    myuf.union(p, q)
                if i < m-1 and grid[i+1][j] == 1:
                    q = p+n
                    myuf.union(p, q)
                if j > 0 and grid[i][j-1] == 1:
                    q = p-1
                    myuf.union(p, q)
                if j < n-1 and grid[i][j+1] == 1:
                    q = p+1
                    myuf.union(p, q)
                    
        return myuf.cnt
        

#dfs solution

class Solution(object):
    def dfs_mark_zero(self, grid, i, j, m, n):
        if i == m or j == n or i < 0 or j < 0:
            return
        
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.dfs_mark_zero(grid, i-1, j, m, n)
        self.dfs_mark_zero(grid, i+1, j, m, n)
        self.dfs_mark_zero(grid, i, j-1, m, n)
        self.dfs_mark_zero(grid, i, j+1, m, n)
        
        return
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        ret = 0
        if m == 0:
            return ret
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ret = ret + 1
                    self.dfs_mark_zero(grid, i, j, m, n)
                    
        return ret


