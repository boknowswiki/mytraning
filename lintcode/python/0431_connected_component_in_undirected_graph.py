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
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        v = set()
        ret = []
        
        for node in nodes:
            #print node.label
            if node not in v:
                self.bfs(node, v, ret)
                
        return ret
        
    def bfs(self, node, v, ret):
        print "in bfs", node.label
        l = []
        q = deque([node])
        v.add(node)
        
        while len(q) > 0:
            cur = q.popleft()
            #print "v add %s" % cur.label
            #v.add(cur)
            l.append(cur.label)
            
            for nei in cur.neighbors:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
        #print "in bfs"            
        #for vv in v:
        #    print vv.label
        
        l.sort()
        #print l
        ret.append(l)
        
        return
    
        
