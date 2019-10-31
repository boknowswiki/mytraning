#!/usr/bin/python -t

# BFS
#解法如下：
#两次BFS：
#1.从0，0（左上）开始BFS，记录0,0到达所有可拓展点的距离。（碰到1还是要记录， 但是1不能继续向外拓展）；
#2.从M - 1, N - 1（右下） 开始BFS， 。。。。。同上
#因为1不能往外拓展，所以很多被包在中间的1的距离矩阵是不会被更新的， 所以有些点的距离矩阵还是Integer.MAX_VALUE, 表示不可到达。
#
#然后得到两个记录距离的矩阵，
#srcToDes矩阵：从左上出发到达每个点的距离（初始Integer.MAX_VALUE表示不可到达）
#DesToSrc矩阵：从右下出发到达每个点的距离（初始Integer.MAX_VALUE表示不可到达）
#
#做完两次BFS得到初始点，终点到达每个点的距离
#
#之后枚举每个点， 如果左上和右下都可以到达这个点（一开始设置为Integer.MAX_VALUE) 如果可以拓展到这个点，
#值会被修改。 如果两个矩阵都可以到达该点， 那么更新最短距离。
#
#if m 接近于 n
#时间复杂度： N^2
#空间复杂度： N^2


from collections import deque

class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        # Write your code here
        m = len(grid)
        n = len(grid[0])
        
        srcToDst = [[sys.maxint]*n for _ in range(m)]
        dstToSrc = [[sys.maxint]*n for _ in range(m)]
        
        self.bfs(0, 0, grid, srcToDst)
        self.bfs(m-1, n-1, grid, dstToSrc)
        
        ret = sys.maxint
        
        for i in range(m):
            for j in range(n):
                if srcToDst[i][j] != sys.maxint and dstToSrc[i][j] != sys.maxint:
                    ret = min(ret, srcToDst[i][j]+dstToSrc[i][j])
                    
        return ret if ret != sys.maxint else -1
        
    def bfs(self, x, y, grid, matrix):
        m = len(grid)
        n = len(grid[0])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        q = deque()
        v = set()
        
        q.append((x, y))
        v.add((x, y))
        
        matrix[x][y] = 1
        steps = 0
        
        while len(q) > 0:
            l = len(q)
            steps += 1
            
            for _ in range(l):
                cx, cy = q.popleft()
                
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    
                    if 0<=nx<m and 0<=ny<n and (nx, ny) not in v:
                        v.add((nx, ny))
                        matrix[nx][ny] = steps
                        
                        if grid[nx][ny] != 1:
                            q.append((nx, ny))
                            
        return
    
    
