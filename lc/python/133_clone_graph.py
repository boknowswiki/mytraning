#!/usr/bin/python -t

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
