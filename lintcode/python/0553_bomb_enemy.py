#!/usr/bin/python -t

# dp solution time O(n^2) space O(n)

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        # 预处理出每个点向四个方向能炸到的人数，然后枚举所有点，取最大值即可
        
        m, n = len(grid), 0
        if m:
            n = len(grid[0])
            
        ret, row = 0, 0
        col = [0 for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    row = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            row += 1
                            
                if i == 0 or grid[i-1][j] == 'W':
                    col[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            col[j] += 1
                            
                if grid[i][j] == '0':
                    ret = max(ret, row+col[j])
                    
        return ret

