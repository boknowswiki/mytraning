# bfs
# time O(n)
# space O(n)

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        ret = [-1] * n
        v = set()
        # -1 means any color, 0 means red, 1 means blue
        for i, j in redEdges:
            graph[i].append((j, 0))
        for i, j in blueEdges:
            graph[i].append((j, 1))

        q = collections.deque([(0, -1, 0)]) # node, color, distance
        v.add((0, -1))
        ret[0] = 0

        while q:
            cur, color, dist = q.popleft()
            for nei, col in graph[cur]:
                if col != color:
                    if ret[nei] == -1:
                        ret[nei] = dist+1
                    
                    if (nei, col) not in v:
                        v.add((nei, col))
                        q.append((nei, col, dist+1))

        return ret
