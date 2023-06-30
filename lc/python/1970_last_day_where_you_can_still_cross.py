# binary search and bfs
# time O(row*col*log(row*col))
# space O(row * col)

import collections

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = 1
        right = len(cells)#row*col

        def can_cross(day):
            grid = [[0]*col for _ in range(row)]
            q = collections.deque()

            for r, c in cells[:day]:
                grid[r-1][c-1] = 1

            for i in range(col):
                if not grid[0][i]:
                    q.append((0, i))
                    grid[0][i] = -1

            while q:
                r, c = q.popleft()
                if r == row-1:
                    return True
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = -1

            return False

        while left < right:
            mid = right-(right-left)//2
            if can_cross(mid):
                left = mid
            else:
                right = mid-1

        return left
