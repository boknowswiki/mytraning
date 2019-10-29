#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        m = len(maze)
        n = len(maze[0])
        
        #print start
        v = set()
        q = deque()
        q.append((start[0], start[1]))
        v.add((start[0], start[1]))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while len(q) > 0:
            cx, cy = q.popleft()
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] == 0:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    
                px = nx - dx[i]
                py = ny - dy[i]
                
                if px == destination[0] and py == destination[1]:
                    return True
                    
                if (px, py) not in v:
                    v.add((px, py))
                    q.append((px, py))
                    
        return False
        
        
