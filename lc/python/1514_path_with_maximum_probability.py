# graph, bfs
# time O(m*n)
# space O(m+n)

import collections

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)

        for i, (a,b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        q = collections.deque([start])

        while q:
            cur = q.popleft()
            for nxt, nxt_prob in graph[cur]:
                if max_prob[cur]*nxt_prob > max_prob[nxt]:
                    q.append(nxt)
                    max_prob[nxt] = max_prob[cur]*nxt_prob

        return max_prob[end]


# graph, bfs with heap
# time O(m+nlogn)
# space O(m+n)


import collections

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]    
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:

                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0
