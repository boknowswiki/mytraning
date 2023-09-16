# bfs and binary search
# time O(mn)
# space O(mn)

import collections

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        def bfs(mid):
            nonlocal m, n, heights
            v = set()
            q = collections.deque([(0, 0)])

            while q:
                x, y = q.pop()
                if x == m-1 and y == n-1:
                    return True
                
                v.add((x, y))
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v:
                        cur_diff = abs(heights[nx][ny] - heights[x][y])
                        if cur_diff <= mid:
                            q.append((nx, ny))


        left = 0
        right = 10000000

        while left < right:
            mid = (left+right)//2
            if bfs(mid):
                right = mid
            else:
                left = mid+1

        return left


# bfs and heap
# time O(mnlog(mn))
# space O(mn)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        difference_matrix = [[math.inf]*col for _ in range(row)]
        difference_matrix[0][0] = 0
        visited = [[False]*col for _ in range(row)]
        queue = [(0, 0, 0)]  # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    max_difference = max(
                        current_difference, difference_matrix[x][y])
                    if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                        difference_matrix[adjacent_x][adjacent_y] = max_difference
                        heapq.heappush(
                            queue, (max_difference, adjacent_x, adjacent_y))
        return difference_matrix[-1][-1]
