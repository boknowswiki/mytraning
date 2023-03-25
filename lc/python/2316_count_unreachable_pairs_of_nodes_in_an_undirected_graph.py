# bfs

import collections

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        q = collections.deque([])
        con = []
        v = set()

        graph = collections.defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def bfs(node):
            nonlocal q, v, con, graph

            level = [node]
            q.append(node)
            v.add(node)

            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
                        level.append(nei)

            return len(level)

        ret = 0
        remaining = n
        for i in range(n):
            if i not in v:
                cnt = bfs(i)
                ret += cnt*(remaining-cnt)
                remaining -= cnt

        return ret


# Time Limit Exceeded
import collections

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        q = collections.deque([])
        con = []
        v = set()

        graph = collections.defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def bfs(node):
            nonlocal q, v, con, graph

            level = [node]
            q.append(node)
            v.add(node)

            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)
                        level.append(nei)

            con.append(len(level))

            return

        for i in range(n):
            if i not in v:
                bfs(i)

        ret = 0
        #print(f"con {con}")
        for i in range(len(con)-1):
            for j in range(i+1, len(con)):
                ret += con[i]*con[j]

        return ret
