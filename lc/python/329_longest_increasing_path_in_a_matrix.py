#!/usr/bin/python -t

# bfs and topology sort

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
	# Step 1: build a directed acyclic graph
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for x, y in neighbors:
                    if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[i][j] < matrix[x][y]:
                        graph[(i,j)].append((x,y))
                        indegree[(x,y)]+=1

        # Step 2: Topological sorting with Kahn's algorithm
        queue = collections.deque([(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if (i,j) not in indegree])
        max_path_len = 0
        while queue:
            max_path_len += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
        return max_path_len

# dp dfs and memorization

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        visited = [[False] * (n) for i in range(m)]
        dp = [[1]* n for i in range(m)]
        ret = 0
        
        for i in range(m):
            for j in range(n):
                dp[i][j] = self.dfs(matrix, i, j, dp, visited)
                ret = max(ret, dp[i][j])
                
        return ret
    
    def dfs(self, matrix, i, j, dp, visited):
        if visited[i][j]:
            return dp[i][j]
        
        m = len(matrix)
        n = len(matrix[0])
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < m and 0<= ny < n:
                if matrix[i][j] > matrix[nx][ny]:
                    dp[i][j] = max(dp[i][j], self.dfs(matrix, nx, ny, dp, visited)+1)
                    
        visited[i][j] = True
        
        return dp[i][j]

