# bfs

import collections

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0

        ret = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def valid(x, y):
            nonlocal m, n, grid
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 0

        def set_to_one(x, y):
            nonlocal grid, dirs
            v = set()
            q = collections.deque([(x, y)])
            v.add((x, y))
            grid[x][y] = 1

            while q:
                cx, cy = q.popleft()
                for i in range(len(dirs)):
                    dx = cx + dirs[i][0]
                    dy = cy + dirs[i][1]
                    if valid(dx, dy) and (dx, dy) not in v:
                        v.add((dx, dy))
                        q.append((dx, dy))
                        grid[dx][dy] = 1

            return

        for i in range(m):
            if grid[i][0] == 0:
                set_to_one(i, 0)
            if grid[i][n-1] == 0:
                set_to_one(i, n-1)

        for j in range(n):
            if grid[0][j] == 0:
                set_to_one(0, j)
            if grid[m-1][j] == 0:
                set_to_one(m-1, j)

        v = set()
        def bfs(x, y):
            nonlocal grid, dirs, v
            q = collections.deque([(x, y)])
            v.add((x, y))

            while q:
                cx, cy = q.popleft()
                for i in range(len(dirs)):
                    dx = cx + dirs[i][0]
                    dy = cy + dirs[i][1]
                    if valid(dx, dy) and (dx, dy) not in v:
                        v.add((dx, dy))
                        q.append((dx, dy))               

            return

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0 and (i, j) not in v:
                    bfs(i, j)
                    ret += 1

        return ret
      
      
class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visit = new boolean[m][n];
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && !visit[i][j] && bfs(i, j, m, n, grid, visit)) {
                    count++;
                }
            }
        }
        return count;
    }

    public boolean bfs(int x, int y, int m, int n, int[][] grid, boolean[][] visit) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visit[x][y] = true;
        boolean isClosed = true;

        int[] dirx = {0, 1, 0, -1};
        int[] diry = {-1, 0, 1, 0};

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            x = temp[0];
            y = temp[1];

            for (int i = 0; i < 4; i++) {
                int r = x +dirx[i];
                int c = y +diry[i];
                if (r < 0 || r >= m || c < 0 || c >= n) {
                    // (x, y) is a boundary cell.
                    isClosed = false;
                } else if (grid[r][c] == 0 && !visit[r][c]) {
                    q.offer(new int[]{r, c});
                    visit[r][c] = true;
                }
            }
        }

        return isClosed;
    }
}
