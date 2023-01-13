# hash map, dfs, string
# time O(n)
# space O(n)

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = collections.defaultdict(list)

        n = len(parent)
        if n < 2:
            return n
        
        for i in range(n):
            graph[parent[i]].append(i)

        ret = 0

        def dfs(cur):
            nonlocal ret, graph, s
            if cur not in graph:
                return 1

            cur_longest = cur_second_longest = 0
            for nei in graph[cur]:
                longth_from_cur = dfs(nei)
                if s[nei] == s[cur]:
                    continue
                if longth_from_cur > cur_longest:
                    cur_second_longest = cur_longest
                    cur_longest = longth_from_cur
                elif longth_from_cur > cur_second_longest:
                    cur_second_longest = longth_from_cur

            ret = max(ret, cur_longest+cur_second_longest+1)

            return cur_longest+1

        dfs(0)

        return ret
