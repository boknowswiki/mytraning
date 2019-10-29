#!/usr/bin/python -t

# BFS:w


import sys
from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        m = len(maze)
        n = len(maze[0])
        
        steps = [[sys.maxint] * n for _ in range(m)]
        q = deque()
        q.append((start[0], start[1], 0))
        #steps[start[0]][start[1]] = 0
        
        #print steps
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while len(q) > 0:
            cx, cy, cl = q.popleft()
            
            if cl >= steps[cx][cy]:
                continue
            
            steps[cx][cy] = cl
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                nl = cl+1
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] != 1:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    nl += 1
                    
                px = nx-dx[i]
                py = ny-dy[i]
                pl = nl-1
                
                q.append((px, py, pl))
                
        #print steps
        
        return steps[destination[0]][destination[1]] if steps[destination[0]][destination[1]] != sys.maxint else -1
        

