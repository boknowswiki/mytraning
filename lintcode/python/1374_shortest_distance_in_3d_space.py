#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param N: the size of space
    @param barriers: an array of coordinates represents the position of the barrier
    @return: the minimum number of steps
    """
    def shortestDistance(self, N, barriers):
        # Write your code here
        if not barriers:
            return 0
            
        for b in barriers:
            if b[0] == b[1] == b[2] == N-1:
                return -1
                
            
        q = deque()
        v = set()
        q.append((0,0,0))
        v.add((0,0,0))
        steps = 0
        
        
        
        while len(q) > 0:
            l = len(q)
            for _ in range(l):
                x, y, z = q.popleft()
                if x == N-1 and  y ==N-1 and z == N-1:
                    return steps
                
                for dx, dy, dz in ((0,0,1), (0,0,-1), (0,1,0),(0,-1,0),(1,0,0), (-1,0,0)):
                    nx, ny, nz = x+dx, y+dy, z+dz
                    
                    if 0<=nx<N and 0<=ny<N and 0<=nz<N and (nx,ny,nz) not in v and [nx, ny, nz] not in barriers:
                            q.append((nx,ny,nz))
                            v.add((nx,ny,nz))
                    
            steps += 1
            
        return -1
        
