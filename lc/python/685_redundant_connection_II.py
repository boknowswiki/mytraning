#!/usr/bin/python -t

#union find solution
# from this link :
#https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

class Solution(object):
    def union(self, a, b):
        self.uf[self.find(b)] = self.find(a)
        
    def find(self, a):
        if self.uf[a] != a:
            self.uf[a] = self.find(self.uf[a])
            
        return self.uf[a]
    
    def detectcircle(self, v):
        self.visited[v] = True
        for i in range(len(self.ad[v])):
            nextv = self.ad[v][i]
            if self.visited[nextv]:
                return (v, nextv)
            ret = self.detectcircle(nextv)
            if ret[0]:
                return ret
        return (None, None)
        
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        self.uf = range(n+1)
        self.ad = [[] for i in range(n+1)]
        hasfather = [False] * (n+1)
        criticalEdge = None
        
        for i, e in enumerate(edges):
            p, c = e[0], e[1]
            self.ad[p].append(c)
            if hasfather[c]:
                criticalEdge = (p, c)
            hasfather[c] = True
            if self.find(p) == self.find(c):
                circleEdge = (p, c)
            self.union(p, c)
            
        if not criticalEdge:
            return circleEdge
        
        self.visited = [False] *(n+1)
        (p, c) = self.detectcircle(criticalEdge[1])
        return (p, c) if p else criticalEdge
