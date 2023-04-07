# bfs
# time O(mn)
# space O(mn)

import collections

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def valid(x, y):
            nonlocal m, n, grid
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        def set_to_zero(x, y):
            nonlocal grid, dirs
            v = set()
            q = collections.deque([(x, y)])
            v.add((x, y))
            grid[x][y] = 0

            while q:
                cx, cy = q.popleft()
                for i in range(len(dirs)):
                    dx = cx + dirs[i][0]
                    dy = cy + dirs[i][1]
                    if valid(dx, dy) and (dx, dy) not in v:
                        v.add((dx, dy))
                        q.append((dx, dy))
                        grid[dx][dy] = 0

            return

        for i in range(m):
            if grid[i][0] == 1:
                set_to_zero(i, 0)
            if grid[i][n-1] == 1:
                set_to_zero(i, n-1)

        for j in range(n):
            if grid[0][j] == 1:
                set_to_zero(0, j)
            if grid[m-1][j] == 1:
                set_to_zero(m-1, j)

        ret = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    ret+=1

        return ret
