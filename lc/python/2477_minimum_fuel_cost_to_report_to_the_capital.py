# dfs
# time O(n)
# space O(n)

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])

        ret = 0

        def dfs(node, parent):
            nonlocal ret, graph, seats

            reps = 1
            if node not in graph:
                return reps

            for child in graph[node]:
                if child != parent:
                    reps += dfs(child, node)

            if node != 0:
                ret += math.ceil(reps/seats)

            return reps
                
        dfs(0, -1)

        return ret
      
 # bfs
# time O(n)
# space O(n)

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        n = len(roads) + 1
        degree = [0] * n

        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
            degree[road[0]] += 1
            degree[road[1]] += 1

        def bfs():
            nonlocal n, graph, degree

            ret = 0

            q = collections.deque([])

            for i in range(1, n):
                if degree[i] == 1:
                    q.append(i)

            reps = [1] * n

            while q:
                cur = q.popleft()
                ret += math.ceil(reps[cur]/seats)

                for child in graph[cur]:
                    degree[child] -= 1
                    reps[child] += reps[cur]
                    if degree[child] == 1 and child != 0:
                        q.append(child)

            return ret

            
        return bfs()
