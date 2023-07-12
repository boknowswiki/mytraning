# graph, topology
# time O(n)
# space O(n)

import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        if n == 0:
            return []

        maps = collections.defaultdict(list)
        ret = []
        q = collections.deque()
        indegree = collections.defaultdict(int)

        for i in range(n):
            for j in graph[i]:
                maps[j].append(i)
                indegree[i] += 1

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n

        while q:
            cur = q.popleft()
            safe[cur] = True

            for nei in maps[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        for i in range(n):
            if safe[i]:
                ret.append(i)

        return ret

# dfs

class Solution:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)

        visit = [False] * n
        inStack = [False] * n

        for i in range(n):
            self.dfs(i, adj, visit, inStack)

        safeNodes = []
        for i in range(n):
            if not inStack[i]:
                safeNodes.append(i)

        return safeNodes
