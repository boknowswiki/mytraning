#!/usr/bin/python -t

class uf(object):
    def __init__(self, n):
        self.father = range(n)
        self.size = [0] * n
        
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


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        
        myuf = uf(n)
        
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    myuf.union(i, j)
                    
        ret = len({myuf.find(i) for i in range(n)})
        return ret

