#!/usr/bin/python -t

# bfs and hash table.
# 两个考点：
# 
# 是否知道怎么根据边来构图和存储图（邻接表）
# 是否知道可以通过 BFS 来确定父子关系

class Solution:
    """
    @param x: The x
    @param y: The y
    @param a: The a
    @param b: The b
    @return: The Answer
    """
    def tree(self, x, y, a, b):
        graph = self.build_graph(x, y)
        parent = self.build_tree(graph)
        
        results = []
        for u, v in zip(a, b):
            if parent[u] == parent[v]:
                results.append(1)
            elif parent[u] == v or parent[v] == u:
                results.append(2)
            else:
                results.append(0)
        return results
    
    def build_graph(self, x, y):
        graph = {}
        for u, v in zip(x, y):
            if u not in graph:
                graph[u] = set()
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)
        return graph
        
    def build_tree(self, graph):
        from collections import deque
        visited = set([1])
        queue = deque([1])
        parent = {1: None}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node
        return parent

# hash table
# 一次dfs预处理出所有的信息，然后回答询问即可

class Solution:
    """
    @param x: The x
    @param y: The y
    @param a: The a
    @param b: The b
    @return: The Answer
    """
    def tree(self, x, y, a, b):
        # Write your code here
        n = len(x) + 1
        f = [0 for i in range(n + 1)]
        g = [[] for i in range(n + 1)]
        sons = [{} for i in range(n + 1)]
        for i in range(len(x)):
            print x[i], y[i]
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
            print g
            
        self.dfs(1, -1, g, f, sons)
        print g, f, sons
        
        ans = [0 for i in range(len(a))]
        for i in range(len(a)):
            if f[a[i]] == f[b[i]]:
                ans[i] = 1
            elif sons[a[i]].has_key(b[i]) or sons[b[i]].has_key(a[i]):
                ans[i] = 2
        return ans
        
    def dfs(self, rt, fa, g, f, sons):
        for x in g[rt]:
            if x == fa:
                continue
            f[x] = rt
            sons[rt][x] = x
            self.dfs(x, rt, g, f, sons)
            
