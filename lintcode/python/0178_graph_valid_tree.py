#!/usr/bin/python3 -t

# bfs
# time O(n)
# space O(n)


from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n != len(edges) + 1:
            return False

        graph = dict()

        for x, y in edges:
            if x not in graph:
                graph[x] = list()
            if y not in graph:
                graph[y] = list()

            graph[x].append(y)
            graph[y].append(x)

        q = [0]
        v = set()
        v.add(0)

        while len(q) > 0:
            cur = q[0]
            q = q[1:]
            if cur in graph:
                for node in graph[cur]:
                    if node not in v:
                        v.add(node)
                        q.append(node)

        return len(v) == n


if __name__ == '__main__':
    s = Solution()
    a = 5
    b = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(s.valid_tree(a, b))

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
        

# dfs

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
            
        if len(edges) != n-1:
            return False
            
        self.graph = self.buildGraph(n, edges)
        v = set()
        
        self.dfs(0, edges, v)
        
        return len(v) == n
        
    def buildGraph(self, n, edges):
        ret = {}
        
        for i in range(n):
            ret[i] = []
            
        for e in edges:
            ret[e[0]].append(e[1])
            ret[e[1]].append(e[0])
            
        return ret
            
    def dfs(self, start, edges, v):
        if start in v:
            return
        
        v.add(start)
        
        for e in self.graph[start]:
            if e in v:
                continue
            self.dfs(e, edges, v)
            
        return
    
