# graph and dfs
# time O(n)
# space O(n)

import collections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n < 2:
            return n
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        v = set()

        def dfs(num):
            nonlocal v
            v.add(num)
            for nei in graph[num]:
                if nei not in v:
                    dfs(nei)

            return

        ret = 0
        for i in range(n):
            if i not in v:
                ret += 1
                dfs(i)

        return ret
