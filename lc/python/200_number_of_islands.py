#!/usr/bin/python -t

# dfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, m, n, i, j)
                    
        return cnt
    
    def dfs(self, grid, m, n, x, y):
        grid[x][y] = "0"
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(dirs)):
            dx = x + dirs[i][0]
            dy = y + dirs[i][1]
            
            if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == "1":
                self.dfs(grid, m, n, dx, dy)
                
        return

# bfs
# time O(m*n)
# space O(m*n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        #print(f"m {m}, n {n}")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    #print(f"get i {i}, j {j}")
                    cnt += 1
                    self.bfs(grid, m, n, i, j)
                    
        return cnt
    
    def bfs(self, grid, m, n, i, j):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v = set()
        v.add((i, j))
        q = collections.deque([(i, j)])
        grid[i][j] = 0
        
        while q:
            x, y = q.popleft()
            for i in range(len(dirs)):
                dx = x + dirs[i][0]
                dy = y + dirs[i][1]
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in v and grid[dx][dy] == "1":
                    v.add((dx, dy))
                    q.append((dx, dy))
                    grid[dx][dy] = "0"
                    
        return

# union find solution
#time O(n) for initial union, find O(logn), total O(mn)
#space O(mn)


class uf(object):
    def __init__(self, grid):
        m = len(grid)
        if m == 0:
            return
        
        n = len(grid[0])
        self.cnt = 0
        self.father = [0] * (m*n)
        self.size = [1] *(m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.cnt = self.cnt+1
                index = i * n + j
                self.father[index] = index
                
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = self.father[qroot]
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = self.father[proot]
            self.size[proot] = self.size[proot] + self.size[qroot]
            
        self.cnt = self.cnt - 1
        
        
    def find(self, p):
        tmp = p
        while p != self.father[p]:
            p = self.father[p]
            
        self.father[tmp] = p
        return p
    
class Solution(object):    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        my_uf = uf(grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                    
                p = i * n + j
                if i > 0 and grid[i-1][j] == '1':
                    q = p - n
                    my_uf.union(p, q)
                    
                if j > 0 and grid[i][j-1] == '1':
                    q = p-1
                    my_uf.union(p, q)
                if i < m - 1 and grid[i+1][j] == '1':
                    q = p + n
                    my_uf.union(p, q)
                if j < n - 1 and grid[i][j+1] == '1':
                    q = p + 1
                    my_uf.union(p, q)
                    
        return my_uf.cnt


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

#bfs solution

    def bfs(self, grid, r, c):
        queue = collections.deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]    
                if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'
