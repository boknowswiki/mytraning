#!/usr/bin/python -t

# bfs
# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        v = dict()
        q = collections.deque([node])
        v[node] = Node(node.val, [])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in v:
                    v[nei] = Node(nei.val, [])
                    q.append(nei)

                v[cur].neighbors.append(v[nei])

        return v[node]
        

# dfs

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.v = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.v:
            return self.v[node]
        
        clone_node = Node(val=node.val)
        self.v[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
                
        return clone_node

# bfs and graph
# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        new_node = Node(node.val, [])
        q = collections.deque([(node, new_node)])
        v = {node: new_node}
        
        while q:
            old, new = q.popleft()
            for nei in old.neighbors:
                if nei not in v:
                    new_nei = Node(nei.val, [])
                    v[nei] = new_nei
                    q.append((nei, new_nei))
                new.neighbors.append(v[nei])
                
        return new_node

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

#DFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(node):
            if node == None:
                return None
            if node in self.d:
                return self.d[node]
            newnode = UndirectedGraphNode(node.label)
            self.d[node] = newnode
            for i in node.neighbors:
                newnode.neighbors.append(dfs(i))

            return newnode

        if node == None:
            return None
        self.d = {}
        return dfs(node)


#BFS
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None

        dup = UndirectedGraphNode(node.label)
        q = deque([(node, dup)])
        s = set()

        while q:
            org, dup = q.popleft()
            if org not in s:
                for nei in org.neighbors:
                    dupnei = UndirectedGraphNode(nei.label)
                    dup.neighbors.append(dupnei)
                    q.append((nei, dupnei))

                s.add(org)

        return dup



    # BFS
    def cloneGraph2(self, node):
        if not node: return
        dup = UndirectedGraphNode(node.label)
        queue = deque([(node, dup)])
        visited = set()

        while queue:
            oriNode, dupNode = queue.popleft()
            if oriNode not in visited:
                for nei in oriNode.neighbors:
                    dupNei = UndirectedGraphNode(nei.label)
                    dupNode.neighbors.append(dupNei)
                    queue.append((nei, dupNei))
                visited.add(oriNode)
        return dup
