#!/usr/bin/python -t

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        
        for i in range(1, n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] ==0 and obstacleGrid[0][i-1] == 1)
        for j in range(1, m):
            obstacleGrid[j][0] = int (obstacleGrid[j][0] == 0 and obstacleGrid[j-1][0] == 1)
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[m-1][n-1]

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])

        l = [0]*(m+1)
        for i in xrange(m+1):
            l[i] = [0]*(n+1)

        l[m-1][n] = 1

        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                l[i][j] = 0 if obstacleGrid[i][j] == 1 \
                            else l[i+1][j] + l[i][j+1]

        return l[0][0]

