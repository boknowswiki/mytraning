#!/usr/bin/python -t

# BFS


from collections import deque
import sys

class Solution:
    """
    @param Maze: 
    @return: nothing
    """
    def Portal(self, Maze):
        # 
        if not Maze or not Maze[0]:
            return 0
            
        m = len(Maze)
        n = len(Maze[0])
        q = deque()
        
        steps = [[sys.maxint] *n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if Maze[i][j] == 'S':
                    steps[i][j] = 0
                    q.append((i, j))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
                    
        while len(q) > 0:
            l = len(q)
            
            for i in range(l):
                cx, cy = q.popleft()
                
                for j in range(4):
                    nx = cx + dx[j]
                    ny = cy + dy[j]
                        
                    if 0<=nx<m and 0<=ny<n and Maze[nx][ny] != '#' and \
                        steps[cx][cy]+1 < steps[nx][ny]:
                            steps[nx][ny] = steps[cx][cy] + 1
                            if Maze[nx][ny] == 'E':
                                return steps[nx][ny]
                            q.append((nx, ny))
                            
        return -1
        
       
