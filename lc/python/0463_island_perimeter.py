
# bfs
# time O(m*n)
# space O(k)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                    break
            if start != None:
                break
                
        q = collections.deque([start])
        v = {start}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ret = 0
        
        while q:
            x, y = q.popleft()
            #print(f"x {x}, y {y}")
            for i in range(len(dirs)):
                dx = x + dirs[i][0]
                dy = y + dirs[i][1]
                if (dx < 0 or dx >= m) or (dy < 0 or dy >= n) or (0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 0):
                    #print(f"dx {dx}, dy {dy} +")
                    ret += 1
                elif  0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1 and (dx, dy) not in v:
                    v.add((dx, dy))
                    q.append((dx, dy))
                    
        return ret
      
# different solution

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def sum_adjacent(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count
