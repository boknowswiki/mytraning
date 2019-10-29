#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms or not rooms[0]:
            return
        
        INF = 2147483647
        q = deque()
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    
        while len(q) > 0:
            l = len(q)
            
            for i in range(l):
                cx, cy = q.popleft()
                
                for j in range(4):
                    nx = cx + dx[j]
                    ny = cy + dy[j]
                    
                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny] == INF:
                        q.append((nx, ny))
                        rooms[nx][ny] = rooms[cx][cy]+1
                        
        return
    
    
