#!/usr/bin/python -t

# heap
# 将矩阵周边的格子都放到堆里，这些格子上面是无法盛水的。
# 每次在堆里挑出一个高度最小的格子 cell，把周围的格子加入到堆里。
# 这些格子被加入堆的时候，计算他们上面的盛水量。
# 
# 盛水量 = cell.height - 这个格子的高度
# 当然如果这个值是负数，盛水量就等于 0。

# O  (  n*m      +         m*n  * log(2n+2m))
#     加入heap              遍历   堆操作

import heapq

class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        m = len(heights)
        if m == 0:
            return 0
        n = len(heights[0])
        if n == 0:
            return 0
            
        self.m = m
        self.n = n
        ret = 0
            
        self.build_border(heights)
        
        while len(self.hq) != 0:
            height, x, y = heapq.heappop(self.hq)
            
            for nx, ny in self.adjacents(x, y):
                ret += max(0, height - heights[nx][ny])
                self.add_border(nx, ny, max(heights[nx][ny], height))
                
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
        
