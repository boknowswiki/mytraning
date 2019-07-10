#!/usr/bin/python -t

class uf(object):
    def __init__(self, n):
        self.father = [0] * n*n
        self.size = [1] * n * n
        
        for i in range(n*n):
            self.father[i] = i
            
        gap = n*n-n
        #union first and last row
        for i in range(n):
            self.father[i] = 0
            self.father[i+gap] = 0
            
        gap = n -1
        #union first and last col
        for i in range(0, n*n, n):
            self.father[i] = 0
            self.father[i+gap] = 0
            
        self.size[0] = n*4-4
        
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
            
    def find(self, p):
        tmp = p
        while p != self.father[p]:
            p = self.father[p]
            
        self.father[tmp] = p
        return p
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
        
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        ret = 1
        m = len(grid)
        
        if m == 0:
            return 0
        
        n = len(grid[0])
        
        myuf = uf(m+1)
        
        for i in range(m):
            for j in range(n):
                s = grid[i][j]
                if s == '/':
                    if myuf.connected(i*(n+1)+j+1, (i+1)*(n+1)+j):
                        ret = ret + 1
                    myuf.union(i*(n+1)+j+1, (i+1)*(n+1)+j)
                elif s == '\\':
                    if myuf.connected(i*(n+1)+j, (i+1)*(n+1)+j+1):
                        ret = ret + 1
                    myuf.union(i*(n+1)+j, (i+1)*(n+1)+j+1)
                else:
                    pass
                
        return ret

