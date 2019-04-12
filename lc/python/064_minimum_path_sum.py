#!/usr/bin/python -t

#time O(mn) space O(m)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        d = m * [grid[0][0]]
        
        for i in range (1, m):
            d[i] = d[i - 1] + grid[i][0]
            
        for j in range(1, n):
            d[0] = d[0] + grid[0][j]
            
            for i in range(1, m):
                d[i] = min(d[i-1], d[i]) + grid[i][j]
                
        return d[m-1]


#time O(mn) space O(mn)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_min(grid, r, c, m, n):
            if r == m or c == n:
                return 2**31
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            
            if self.d[r][c] > 0:
                return self.d[r][c]
            
            self.d[r][c] = min(get_min(grid, r + 1, c, m, n), get_min(grid, r, c + 1, m, n)) + grid[r][c]
            return self.d[r][c]
        
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]

        self.d = [0]* m
        for i in range(m):
            self.d[i] = [0] * n
            
        return grid[0][0] + min(get_min(grid, 1, 0, m, n), get_min(grid, 0, 1, m, n))

