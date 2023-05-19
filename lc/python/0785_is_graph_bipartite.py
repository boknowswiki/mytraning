# bfs
# time O(n)
# space O(n)

import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for node in range(n):
            if color[node] != 0:
                continue

            q = collections.deque()
            q.append(node)
            color[node] = 1

            while q:
                cur = q.popleft()

                for nei in graph[cur]:
                    if color[nei] == 0:
                        color[nei] = -color[cur]
                        q.append(nei)
                    elif color[nei] != -color[cur]:
                        return False


        return True
      
# dfs

class Solution:
    def validColouring(self, gr, colour, node, col):
        if colour[node] != 0:
            return colour[node] == col

        colour[node] = col
        for ne in gr[node]:
            if not self.validColouring(gr, colour, ne, -col):
                return False

        return True

    def isBipartite(self, gr):
        n = len(gr)
        colour = [0] * n

        for node in range(n):
            if colour[node] == 0 and not self.validColouring(gr, colour, node, 1):
                return False

        return True
