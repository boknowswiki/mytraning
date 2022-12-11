# heapq and bfs

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        if m == 0:
            return 0
        n = len(heightMap[0])
        if n == 0:
            return 0
            
        self.m = m
        self.n = n
        ret = 0
            
        self.build_border(heightMap)
        
        while len(self.hq) != 0:
            height, x, y = heapq.heappop(self.hq)
            
            for nx, ny in self.adjacents(x, y):
                ret += max(0, height - heightMap[nx][ny])
                self.add_border(nx, ny, max(heightMap[nx][ny], height))
                
        return ret
    
    def build_border(self, heights):
        self.hq = []
        self.v = set()
        
        for i in range(self.m):
            self.add_border(i, 0, heights[i][0])
            self.add_border(i, self.n-1, heights[i][self.n-1])
            
        for j in range(self.n):
            self.add_border(0, j, heights[0][j])
            self.add_border(self.m-1, j, heights[self.m-1][j])
            
        return
        
        
    def add_border(self, x, y, height):
        heapq.heappush(self.hq, (height, x, y))
        self.v.add((x,y))
        
        return
    
        
    def adjacents(self, x, y):
        neis = []
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            
            if 0 <= cx < self.m and 0 <= cy < self.n and (cx, cy) not in self.v:
                neis.append((cx, cy))
                
        return neis
