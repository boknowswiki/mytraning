# bfs


import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        v = set()
        for road in roads:
            graph[road[0]].append([road[1], road[2]])
            graph[road[1]].append([road[0], road[2]])

        q = collections.deque([1])
        ret = sys.maxsize

        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                if (cur, nei[0]) not in v:
                    ret = min(ret, nei[1])
                    v.add((cur, nei[0]))
                    v.add((nei[0], cur)) # add this line passed
                    q.append(nei[0])

        return ret

# Time Limit Exceeded
import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        v = set()
        for road in roads:
            graph[road[0]].append([road[1], road[2]])
            graph[road[1]].append([road[0], road[2]])

        q = collections.deque([1])
        ret = sys.maxsize

        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                if (cur, nei[0]) not in v:
                    ret = min(ret, nei[1])
                    v.add((cur, nei[0]))
                    q.append(nei[0])

        return ret
