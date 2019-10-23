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
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
            
        nodes_indent = self.get_nodes_indent(graph)
            
        start_node = [i for i in graph if nodes_indent[i] == 0 ]
        ret = []
        q = deque(start_node)
        
        while len(q) > 0:
            cur = q.popleft()
            ret.append(cur)
            
            for nei in cur.neighbors:
                nodes_indent[nei] -= 1
                if nodes_indent[nei] == 0:
                    q.append(nei)
                
        return ret
        
    def get_nodes_indent(self, graph):
        nodes_indent = {i:0 for i in graph}
        
        for node in graph:
            for nei in node.neighbors:
                nodes_indent[nei] += 1
                
        return nodes_indent
        
# DFS

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        indegree = {}
        for x in graph:
            indegree[x] = 0

        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1

        ans = []
        for i in graph:
            if indegree[i] == 0:
                self.dfs(i, indegree, ans)
        return ans
    
    def dfs(self, i, indegree, ans):
        ans.append(i)
        indegree[i] -= 1
        for j in i.neighbors:
            indegree[j] -= 1
            if indegree[j] == 0:
                self.dfs(j, indegree, ans)
