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

# dfs

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
            # Create adjacency list
        adj = [[] for _ in range(len(colors))]
        for s, e in edges:
            adj[s].append(e)

        # Initialize result variable and cache array
        res = 0
        cache = [None for _ in range(len(colors))]

        # Define DFS function to traverse the graph
        def dfs(current, visited):
            # If we have already visited this node in the current path, we are in a cycle
            if current in visited:
                return None
            # If we have already computed the result for this node, return it from the cache
            if cache[current] is not None:
                return cache[current]
            # Mark the current node as visited
            visited.add(current)

            # Initialize a dictionary to store the maximum count of each color seen so far
            res = {}
            # Traverse all the neighbors of the current node
            for con in adj[current]:
                # Recursively call the DFS function on the neighbor
                child_res = dfs(con, visited)
                # If we encounter a cycle, return None
                if child_res is None:
                    return None
                # Update the maximum count of each color seen so far
                for color, value in child_res.items():
                    res[color] = max(res.get(color, 0), value)

            # Remove the current node from the visited set
            visited.remove(current)

            # Update the count of the current node's color in the result dictionary
            currentColor = colors[current]
            res[currentColor] = res.get(currentColor, 0) + 1

            # Store the result in the cache and return it
            cache[current] = res
            return res

        # Traverse the graph using DFS and update the result variable
        response = 0
        for i in range(len(colors)):
            temp = dfs(i, set())
            # If we encounter a cycle, return -1
            if temp == None:
                return -1
            # Update the result variable with the maximum count of any color seen so far
            response = max(response, max(temp.values()))

        # Return the final result
        return response
