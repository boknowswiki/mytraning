# topology sort

import collections

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        indegree = [0] * len(colors)
        for u, v in edges:
            graph[v].append(u)
            indegree[u] += 1
        
        count = [collections.defaultdict(int) for _ in range(n)]
        q = collections.deque(filter(lambda i: not indegree[i], range(n)))
        seen = 0
        ans = 0
        while q:
            curr = q.popleft()
            count[curr][colors[curr]] += 1
            ans = max(ans, count[curr][colors[curr]])
            seen += 1

            for v in graph[curr]:
                for c in count[curr]:
                    count[v][c] = max(count[v][c], count[curr][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return -1 if seen < n else ans

import collections

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
      n, k = len(colors), 26
      indegrees = [0] * n
      graph = collections.defaultdict(list)
      for u, v in edges:
          graph[u].append(v)
          indegrees[v] += 1
      zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
      counts = [[0] * k for _ in range(n)]
      for i, c in enumerate(colors):
          counts[i][ord(c) - ord('a')] += 1
      max_count, visited = 0, 0
      while zero_indegree:
          u = zero_indegree.pop()
          visited += 1
          for v in graph[u]:
              for i in range(k):
                  counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
              indegrees[v] -= 1
              if indegrees[v] == 0:
                  zero_indegree.add(v)
          max_count = max(max_count, max(counts[u]))
      return max_count if visited == n else -1
