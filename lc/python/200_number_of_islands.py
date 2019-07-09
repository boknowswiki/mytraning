#!/usr/bin/python -t

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

