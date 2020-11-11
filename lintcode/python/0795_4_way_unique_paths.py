#!/usr/bin/python -t

class Solution:
    """
    @param m: the row
    @param n: the column
    @return: the possible unique paths
    """
    def uniquePaths(self, m, n):
        # Write your code here
        self.result =  0
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        def dfs(x, y):
            if x == n - 1 and y == m - 1:
                self.result += 1
                return
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < n and 0 <= y_ < m and not visited[x_][y_]:
                    visited[x_][y_] = 1
                    dfs(x_, y_)
                    visited[x_][y_] = 0
        dfs(0, 0)
        return self.result
