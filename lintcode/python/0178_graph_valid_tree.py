#!/usr/bin/python -t

# union find set

class uf(object):
    def __init__(self, n):
        self.father = {i : i for i in range(n)}
        self.size = [1] * n
        
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot == yroot:
            return
        
        if self.size[xroot] < self.size[yroot]:
            self.father[xroot] = self.father[yroot]
            self.size[yroot] += self.size[xroot]
        else:
            self.father[yroot] = self.father[xroot]
            self.size[xroot] += self.size[yroot]
            
        return
    
    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
            
        return self.father[x]
    

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here

        if len(edges) != n-1:
            return False
            
        myuf = uf(n)
        
        for x, y in edges:
            if myuf.find(x) == myuf.find(y):
                return False
            myuf.union(x, y)
        
        return True
        

# BFS


import collections

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    
    def validTree(self, n, edges):
        # write your code here
        if len(edges) +1 != n:
            return False
            
        neighs = collections.defaultdict(list)
        
        for x, y in edges:
            neighs[x].append(y)
            neighs[y].append(x)
            
        q = collections.deque()
        q.append(0)
        v = {}
        v[0] = True
        
        while len(q) > 0:
            cur = q.popleft()
            v[cur] = True
            for node in neighs[cur]:
                if node not in v:
                    v[node] = True
                    q.append(node)
        #print len(v)            
        return len(v) == n
        