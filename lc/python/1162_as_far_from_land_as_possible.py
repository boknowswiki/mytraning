# bfs
# time O(nm)
# space O(mn)

import collections

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m == 0 or n == 0:
            return -1

        ret = -1

        q = collections.deque([])
        v = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    v.add((i, j))
                    q.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for k in range(len(dirs)):
                    dx = x + dirs[k][0]
                    dy = y + dirs[k][1]
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in v:
                        v.add((dx, dy))
                        q.append((dx, dy))

            ret += 1

        return ret if ret != 0 else -1
