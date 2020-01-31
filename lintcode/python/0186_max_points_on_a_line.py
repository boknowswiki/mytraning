#!/usr/bin/python -t

# hash table

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: an array of point
    @return: An integer
    """
    def maxPoints(self, points):
        # write your code here
        if not points:
            return 0
            
        n = len(points)
        ret = 0
        
        for i in range(n):
            mapping = {}
            vertical, dup, max_val = 0, 0, 0
            
            for j in range(i+1, n):
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        dup += 1
                    else:
                        vertical += 1
                        
                    continue
                
                scope = float(points[j].y - points[i].y)/(points[j].x - points[i].x)
                mapping[scope] = mapping.get(scope, 0) + 1
                max_val = max(max_val, mapping[scope])
            max_val = max(max_val, vertical)
            ret = max(ret, max_val + dup + 1)
            
        return ret
        
        
