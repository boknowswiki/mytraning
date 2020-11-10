#!/usr/bin/python -t

class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        ret = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = set()
                    self.dfs(grid, i, j, shape)
                    ret.add(self.getunique(shape))
                    
        return len(ret)
        
    def dfs(self, grid, x, y, shape):
        shape.add((x, y))
        grid[x][y] = 0
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and grid[cx][cy] == 1:
                self.dfs(grid, cx, cy, shape)
                
        return
    
    def getunique(self, shape):
        dx = [1, 1, -1, -1]
        dy = [1, -1, 1, -1]
        

        all_l = []
        
        for i in range(4):
            l1 = []
            l2 = []
            for s in shape:
                cx = s[0]*dx[i]
                cy = s[1]*dy[i]
                l1.append((cx, cy))
                l2.append((cy, cx))
                
            all_l.append(self.get_str(l1))
            all_l.append(self.get_str(l2))
            
        all_l.sort()
            
        print all_l[0]
        return all_l[0]
        
    def get_str(self, l):
        l.sort()
        x = l[0][0]
        y = l[0][1]
        s = ""
        
        for nx, ny in l:
            s += str((nx-x) + (ny-y))
            
        return s
