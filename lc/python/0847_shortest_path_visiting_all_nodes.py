# bfs, graph
# time O(2^n * n^2)
# space O(2^n * n)

import collections

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        end_mask = (1 << n) - 1
        q = collections.deque([(node, 1 << node) for node in range(n)])
        v = set(q)
        ret = 0

        while q:
            for i in range(len(q)):
                cur, cur_mask = q.popleft()
                for nei in graph[cur]:
                    nei_mask = cur_mask | (1 << nei)
                    if nei_mask == end_mask:
                        return ret + 1
                    
                    if (nei, nei_mask) not in v:
                        v.add((nei, nei_mask))
                        q.append((nei, nei_mask))
            
            ret += 1

        return -1
