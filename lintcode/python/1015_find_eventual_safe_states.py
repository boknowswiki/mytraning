#!/usr/bin/python -t

# BFS

class Solution:
    """
    @param graph: a 2D integers array
    @return: return a list of integers
    """
    def eventualSafeNodes(self, graph):
        # write your code here
        n = len(graph)
        outdegrees = [0 for _ in range(n)]
        parents = {}
        for i in range(n):
            for x in graph[i]:
                if x not in parents:
                    parents[x] = []
                parents[x].append(i)
                outdegrees[i] += 1

        queue = collections.deque()
        for i in range(n):
            if outdegrees[i] == 0:
                queue.append(i)
        res = []
        visited = {}
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited[node] = True
            res.append(node)
            if node not in parents:
                continue
            for p in parents[node]:
                outdegrees[p] -= 1
                if outdegrees[p] == 0:
                    queue.append(p)
                    
        return sorted(res)
        
        
