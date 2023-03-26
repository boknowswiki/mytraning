# bfs

import collections

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])

        #print(f"graph {graph}")
        v = set()
        ret = -1

        def bfs(node):
            nonlocal graph, v, ret
            #print(f"node {node}")
            q = collections.deque([node])
            v.add(node)
            path = [node]
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    #print(f"cur {cur}, nei {nei}, path {path}, v {v}")
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
                        path.append(nei)
                    else:
                        if nei in path:
                            index = path.index(nei)
                            ret = max(ret, len(path)-index)

            return

        for i in range(len(edges)):
            if i not in v:
                bfs(i)

        return ret
