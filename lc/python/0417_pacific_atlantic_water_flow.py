# bfs
# time O(mn)
# space O(mn)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs(q):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            v = set(q)
            dq = collections.deque(q)
            
            while dq:
                x, y = dq.popleft()
                for i in range(len(dirs)):
                    dx = x + dirs[i][0]
                    dy = y + dirs[i][1]
                    if 0 <= dx < m and 0 <= dy < n and heights[dx][dy] >= heights[x][y] and (dx, dy) not in v:
                        v.add((dx, dy))
                        dq.append((dx, dy))
                        
            return v
            
        pacific = [(i, 0) for i in range(m)] + [(0, i) for i in range(1, n)]
        atlantic = [(i, n-1) for i in range(m)] + [(m-1, i) for i in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)
