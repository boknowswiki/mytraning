#!/usr/bin/python -t

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
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        root = node
        if not node:
            return node
            
        nodes = self.getNodes(node)
        mapping = {}
        
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
            
        for node in nodes:
            new_node = mapping[node]
            for neigh in node.neighbors:
                new_neigh = mapping[neigh]
                new_node.neighbors.append(new_neigh)
                
        return mapping[root]
        
        
        
    def getNodes(self, node):
        q = collections.deque([node])
        ret = set([node])

        # output is 1
        #for e in q:
        #    print e.label
        
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in ret:
                    ret.add(neighbor)
                    q.append(neighbor)
                    
        return ret
        
if __name__ == '__main__':
    s = {1,2,4#2,1,4#4,1,2}
    ss = Solution()
    print "answer is\n"
    print ss.cloneGraph(s, v)
