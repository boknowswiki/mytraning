#!/usr/bin/python -t

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

