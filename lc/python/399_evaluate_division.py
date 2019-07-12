#!/usr/bin/python -t

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def find(x):
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]
    
        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry: return -1.0
            return vx / vy
        
        U = {}
        for (x, y), v in zip(equations, values):      
            if x not in U and y not in U:
                U[x] = (y, v)
                U[y] = (y, 1.0)
            elif x not in U:
                U[x] = (y, v)
            elif y not in U:
                U[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                U[rx] = (ry, v / vx * vy)
    
        ans = [divide(x, y) if x in U and y in U else -1 for x, y in queries]
        return ans

