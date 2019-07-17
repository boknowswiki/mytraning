#!/usr/bin/python -t

#better union find solution

class uf(object):
    def __init__(self, n):
        self.p = {i : i for i in range(n)}
        
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            
        return self.p[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot != yroot:
            self.p[xroot] = yroot
            return False
        else:
            return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        myuf = uf(1001)
        
        for e in edges:
            if myuf.union(e[0], e[1]):
                return e

#combine union and connected to one function:

class uf(object):
    def __init__(self):
        self.father = range(1001)
        self.size = [1] * 1001
        
    def find(self, p):
        tmp = p
        
        while p != self.father[p]:
            p = self.father[p]
            
        self.father[tmp] = p
        
        return p
    
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return False
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = qroot
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = proot
            self.size[proot] = self.size[proot] + self.size[qroot]
            
        return True
            
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        myuf = uf()
        
        for e in edges:
            if not myuf.union(*e):
                return e

#org solution

class uf(object):
    def __init__(self):
        self.father = range(1001)
        self.size = [1] * 1001
        
    def find(self, p):
        tmp = p
        
        while p != self.father[p]:
            p = self.father[p]
            
        self.father[tmp] = p
        
        return p
    
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = qroot
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = proot
            self.size[proot] = self.size[proot] + self.size[qroot]
            
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        myuf = uf()
        
        for e in edges:
            if myuf.connected(e[0], e[1]):
                return e
            else:
                myuf.union(e[0], e[1])

