#!/usr/bin/python -t

# BFS

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        if s == t:
            return True
        
        v = set()    
        q = deque([s])
        v.add(s)
        
        while len(q) > 0:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                if node == t:
                    return True
                for nei in node.neighbors:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
                        
        return False
        

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# DFS

class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        visited = set()
        return self.dfs(graph, s, t, s, visited)
        
    def dfs(self, graph, s, t, cur, visited):
        if cur in visited:
            return False
        if cur == t:
            return True
        visited.add(cur)
        for nei in graph[cur.label].neighbors:
            if self.dfs(graph, s, t, nei, visited):
                return True
        return False
