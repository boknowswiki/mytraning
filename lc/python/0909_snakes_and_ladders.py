# bfs and matrix
# time O(n^2)
# space O(n)

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None]* (n**2+1)
        label = 1
        columns = list(range(0, n))

        for row in range(n-1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()

        dist = [-1] * (n**2+1)
        q = deque([1])
        dist[1] = 0

        while q:
            cur = q.popleft()
            for nxt in range(cur+1, min(cur+6, n**2)+1):
                row, col = cells[nxt]
                dest = board[row][col] if board[row][col] != -1 else nxt

                if dist[dest] == -1:
                    dist[dest] = dist[cur] + 1
                    q.append(dest)

        return dist[n**2]
      
      
# time O(n^2*logn)
# space O(n)
      
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        dist[1] = 0
        q = [(0, 1)]
        while q:
            d, curr = heapq.heappop(q)
            if d != dist[curr]:
                continue
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1 or dist[curr] + 1 < dist[destination]:
                    dist[destination] = dist[curr] + 1
                    heapq.heappush(q, (dist[destination], destination))
        return dist[n * n]
