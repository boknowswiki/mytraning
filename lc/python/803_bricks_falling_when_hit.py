#!/usr/bin/python -t

# reverse union find solution

class uf(object):
    def __init__(self, R, C):
        self.p = range(R*C+1)
        self.sz = [1] * (R*C+1)
        
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr != yr:
            self.p[xr] = yr
            self.sz[yr] += self.sz[xr]
            
    def size(self, x):
        return self.sz[self.find(x)]
    
    def top(self):
        return self.size(len(self.sz)-1)-1

class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        R, C = len(grid), len(grid[0])
        
        def index(r, c):
            return r*C + c
        
        def neighbors(r, c):
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0<= nr < R and 0 <= nc < C:
                    yield nr, nc
                    
        myuf = uf(R, C)
        
        A = [row[:] for row in grid]
        
        for i, j in hits:
            A[i][j] = 0
                    
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        myuf.union(i, R*C)
                    if r and A[r-1][c]:
                        myuf.union(i, index(r-1,c))
                    if c and A[r][c-1]:
                        myuf.union(i, index(r, c-1))
                        
        ans = []
        for r, c in reversed(hits):
            pre_roof = myuf.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        myuf.union(i, index(nr,nc))
                if r == 0:
                    myuf.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, myuf.top()-pre_roof-1))
                
        return ans[::-1]

