#!/usr/bin/python -t

# BFS 


from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
            
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] or grid[m-1][n-1]:
            return -1
            
        v = set()
        q = deque()
        q.append((0, 0))
        v.add((0, 0))
        
        dx = [1, -1, 2, -2]
        dy = [2, 2, 1, 1]
        ret = 0
        while len(q) > 0:
            l = len(q)
            ret += 1
            
            for i in range(l):
                cx, cy = q.popleft()
                for j in range(4):
                    nx = cx+dx[j]
                    ny = cy+dy[j]
                    
                    if nx == m-1 and ny == n-1:
                        return ret
                        
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 0 and (nx, ny) not in v:
                        q.append((nx, ny))
                        v.add((nx, ny))
            
        return -1
        
          

# dp solution, time O(mn) space(mn)

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        # dp[i][j] the minimum path from [0,0] to [i,j]
        # dp[i][j] = min(dp[i-1][j-2], dp[i+1][j-2], dp[i-2][j-1], dp[i+2][j-1]) + 1
        # dp[i][j] = sys.maxint, dp[0][0] = 0
        # dp[m-1][n-1]
        #进行循环的时候需要先循环列，再循环行因为：
        #
        #骑士行走的方向在行方向是无序的（可以先走到i - 2然后又走回i + 2），而在列方向是有序的（只能走到
        #i + 1或者i + 2）,所以在列方向无循环依赖，在行方向有循环依赖，所以在循环时要先循环列，这样每走到
        #一列时此列前面的所有列中的元素都已经被循环过了，而在后面列的元素全都没有循环过的情况下，此行的
        #并不依赖于后面行的元素。若先循环行，循环到某一行时，前面行的元素都用过了，后面行的元素虽然没被
        #用过，但是此行需要后面行的元素来判断此行的元素是否需要改变，而后面行的元素都是初始化的值，故出
        #来的答案肯定是错的。
        
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        if grid[0][0] == 1:
            return -1
            
        dp = [[sys.maxint]*n for i in range(m)]
        direct = [(-1, -2), (1, -2), (-2, -1), (2, -1),]
        dp[0][0] = 0
        
        for j in range(n):
            for i in range(m):
                if grid[i][j] != 1:
                    for k in range(4):
                        nx = i + direct[k][0]
                        ny = j + direct[k][1]
                        if (0<=nx<m) and (0<=ny<n):
                            dp[i][j] = min(dp[i][j], dp[nx][ny]+1)
        #print dp                    
        return dp[m-1][n-1] if dp[m-1][n-1] != sys.maxint else -1

