#!/usr/bin/python -t


#union find solution

class uf(object):
    def __init__(self, n):
        self.father = [0] * (n*n)
        self.size = [1] * (n*n)
        
        for i in range(n):
            for j in range(n):
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
            
        return
        
    def find(self, p):
        tmp = p
        while p != self.father[p]:
            p = self.father[p]
        
        self.father[tmp] = p
        return p
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)


#class uf(object):
#    def __init__(self, n):
#        self.father = {i : i for i in range(n)}
#        
#    def find(self, p):
#        #tmp = p
#        if self.father[p] != p:
#            self.father[p] = self.father[self.father[p]]
#            p = self.father[p]
#            
#        #self.father[tmp] = p
#        
#        return p
#    
#    def iscon(self, p, q):
#        return self.find(p) == self.find(q)
#    
#    def union(self, p, q):
#        proot = self.find(p)
#        qroot = self.find(q)
#        if proot == qroot:
#            return
#        self.father[proot] = self.father[qroot]
        

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        myuf = uf(n*n)
        time = 0
        
        while not myuf.connected(0, n*n-1):
            for i in range(n):
                for j in range(n):
                    if grid[i][j] > time:
                        continue
                    if i < n - 1 and grid[i+1][j] <= time:
                        myuf.union(i*n+j, i*n+j+n)
                    if j < n - 1 and grid[i][j+1] <= time:
                        myuf.union(i*n+j, i*n+j+1)
            time = time + 1
            
        return time - 1

if __name__ =='__main__':
    #s = [[0,2],[1,3]]
    s = [[6,22,3,23,1],[14,8,7,16,5],[11,0,9,15,18],[24,4,2,13,19],[20,10,17,21,12]]
    ss = Solution()
    print('answer is %d' % ss.swimInWater(s))

