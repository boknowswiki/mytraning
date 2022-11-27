# dfs
# time O(m*n)
# space O(m*n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        if old != color:
            v = {(sr, sc)}
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            def dfs(x, y):
                image[x][y] = color
                for i in range(len(dirs)):
                    dx = x + dirs[i][0]
                    dy = y + dirs[i][1]
                    
                    if 0 <= dx < len(image) and 0 <= dy < len(image[0]) and (dx, dy) not in v and image[dx][dy] == old:
                        v.add((dx, dy))
                        dfs(dx, dy)
            
            dfs(sr, sc)
            
        return image

# bfs
# time O(m*n)
# space O(m*n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = color
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image
