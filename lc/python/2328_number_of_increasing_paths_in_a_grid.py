# dfs and momerization
# time O(m*n)
# space O(m*n)

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        dp = [[0]*n for _ in range(m)]

        def dfs(i, j):
            nonlocal dp, directions, mod

            if dp[i][j]:
                return dp[i][j]

            ret = 1

            for x, y in directions:
                dx, dy = x + i, y + j
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] > grid[i][j]:
                    ret += dfs(dx, dy) % mod

            dp[i][j] = ret

            return ret


        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
