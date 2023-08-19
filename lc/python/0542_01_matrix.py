# bfs, matrix
# time O(m*n)
# space O(m*n)

import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row[:] for row in mat]
        m, n = len(matrix), len(matrix[0])
        q = collections.deque()
        v = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    q.append((row, col, 0))
                    v.add((row, col))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            row, col, dist = q.popleft()
            for dr, dc in dirs:
                next_row = row + dr
                next_col = col + dc

                if 0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in v:
                    v.add((next_row, next_col))
                    q.append((next_row, next_col, dist+1))
                    matrix[next_row][next_col] = dist+1

        return matrix
