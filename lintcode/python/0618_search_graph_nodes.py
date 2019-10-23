#!/usr/bin/python -t

# BFS

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        if values[node] == target:
            return node
            
        q = deque([node])
        v = set()
        v.add(node)
        
        while len(q) > 0:
            cur = q.popleft()
            
            if values[cur] == target:
                return cur
                
            for nei in cur.neighbors:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
                    
        return None
        
     
