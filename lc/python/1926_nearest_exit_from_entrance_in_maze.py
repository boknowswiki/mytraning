# bfs


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = collections.deque([(entrance[0], entrance[1])])
        v = {(entrance[0], entrance[1])}
        cnt = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def is_exit(x, y):
            if maze[x][y] == "." and (x == 0 or x == m-1 or y == 0 or y == n-1) and ((x != entrance[0]) or (y != entrance[1])):
                return True
            return False
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if is_exit(x, y):
                    return cnt
                
                for i in range(len(dirs)):
                    dx = x + dirs[i][0]
                    dy = y + dirs[i][1]
                    if 0 <= dx < m and 0 <= dy < n and maze[dx][dy] == "." and (dx, dy) not in v:
                        v.add((dx, dy))
                        q.append((dx, dy))
            cnt += 1
            
        return -1
