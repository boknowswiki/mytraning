#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param height: the Cable car station height
    @return: the longest time that he can ride
    """
    def cableCarRide(self, height):
        # Write your code here
        if not height or not height[0]:
            return 0
            
        ret = 0
        m = len(height)
        n = len(height[0])
        
        for i in range(m):
            for j in range(n):
                length = self.dfs(i, j, m, n, height)
                ret = max(length, ret)
                
        return ret
        
    def dfs(self, x, y, m, n, height):
        ret = 0
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<m and 0<=ny<n and height[nx][ny] > height[x][y]:
                length = self.dfs(nx, ny, m, n, height)
                ret = max(ret, length)
                
        return ret + 1
        
        
