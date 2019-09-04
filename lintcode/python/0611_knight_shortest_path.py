#!/usr/bin/python -t

# bfs solution, time O(mn) space O(mn)

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        # bfs
        
        m = len(grid)
        if m == 0:
            return -1
            
        n = len(grid[0])
        if n == 0:
            return -1
            
        if source.x == destination.x and source.y == destination.y:
            return 0
            
        nx = [1, 1, -1, -1, 2, 2, -2, -2]
        ny = [2, -2, 2, -2, 1, -1, 1, -1]
        v = [[False] * (n) for i in range(m)]
        v[source.x][source.y] = True
        dist = 0
        q = [(source.x, source.y)]
        #print len(q)
        while len(q)!= 0:
            dist += 1
            s = len(q)
            for i in range(s):
                #print i
                x, y = q.pop(0)
                #print x, y
                for k in range(8):
                    dx = x+nx[k]
                    dy = y+ny[k]
                    print dx, dy
                    if (0<=dx<m) and (0<=dy<n) and (not grid[dx][dy]) and (not v[dx][dy]):
                        if dx == destination.x and dy == destination.y:
                            return dist
                        v[dx][dy] = True
                        q.append((dx,dy))
                        
        #print v
                        
        return -1

