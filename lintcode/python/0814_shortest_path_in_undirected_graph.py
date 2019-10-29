#!/usr/bin/python -t

# BFS

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        # Write your code here
        q = deque()
        v = set()
        
        q.append(A)
        v.add(A)
        steps = 0
        
        while len(q) > 0:
            l = len(q)
            steps += 1
            
            for i in range(l):
                node = q.popleft()
                
                for nei in node.neighbors:
                    if nei == B:
                        return steps
                        
                    if nei in v:
                        continue
                    
                    q.append(nei)
                    v.add(nei)
                    
        return -1
        
        
