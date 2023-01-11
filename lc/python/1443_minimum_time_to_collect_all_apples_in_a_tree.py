# dfs, hash map
# time O(n)
# space O(n)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal hasApple, graph
            if node not in graph:
                return 0

            total = child = 0

            for nei in graph[node]:
                if nei == parent:
                    continue
                child = dfs(nei, node)
                if child > 0 or hasApple[nei]:
                    total += child + 2
                    #print(f"nei {nei}, node {node}, child {child}, total {total}")
                    #print(f"hasApple {hasApple}")

            return total

        print(f"hasApple {hasApple}")
        return dfs(0, -1)
