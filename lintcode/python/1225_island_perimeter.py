#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += self.check_valid_sides(grid, i, j)
                    
        return ret
        
    def check_valid_sides(self, grid, i, j):
        top = 1 - grid[i-1][j] if i-1 >= 0 else 1
        bottom = 1 - grid[i+1][j] if i+1 < len(grid) else 1
        left = 1 - grid[i][j-1] if j -1 >= 0 else 1
        right = 1 - grid[i][j+1] if j+1 < len(grid[0]) else 1
        
        return top+bottom+left+right
        
        
