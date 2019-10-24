#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        v = set()
        q = deque([(0, 0)])
        v.add((0, 0))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while len(q) > 0:
            x, y = q.popleft()
            
            for i in range(4):
                cx, cy = x+dx[i], y+dy[i]
                
                if self.is_valid(map, cx, cy):
                    if map[cx][cy] == 9:
                        return True
                    if map[cx][cy] == 1 and ((cx, cy) not in v):
                        v.add((cx, cy))
                        q.append((cx, cy))
                        
        return False
                        
                    
                    
    def is_valid(self, map, x, y):
        m = len(map)
        n = len(map[0])
        
        if 0<=x<m and 0<=y<n:
            return True
        return False
        
        
