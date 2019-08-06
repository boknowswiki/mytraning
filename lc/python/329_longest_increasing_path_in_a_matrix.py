#!/usr/bin/python -t

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

