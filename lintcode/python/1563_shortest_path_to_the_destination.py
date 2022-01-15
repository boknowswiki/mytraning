#!/usr/bin/python -t

# bfs


from collections import deque

DIRECTIONS = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]


class Solution:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        queue = deque([(0, 0)])
        distance = {(0, 0): 0}
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                _x = x + delta_x
                _y = y + delta_y
                if not self.is_valid(_x, _y, targetMap, distance):
                    continue

                queue.append((_x, _y))
                distance[(_x, _y)] = distance[(x, y)] + 1

                if targetMap[_x][_y] == 2:
                    return distance[(_x, _y)]

        return -1

    def is_valid(self, x, y, targetMap, distance):
        if not 0 <= x < len(targetMap) or not 0 <= y < len(targetMap[0]):
            return False
        return targetMap[x][y] != 1 and (x, y) not in distance


# bfs


import collections

class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        m = len(targetMap)
        if m == 0:
            return 0
        n = len(targetMap[0])

        v = set()
        q = collections.deque()
        q.append((0, 0))
        v.add((0, 0))
        ret = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # print(q)

        while q:
            l = len(q)
            ret += 1
            for i in range(l):
                x, y = q.popleft()
                if targetMap[x][y] == 2:
                    return ret-1
                for j in range(len(dirs)):
                    nx = x + dirs[j][0]
                    ny = y + dirs[j][1]
                    if self.isValid(m, n, nx, ny) and (nx, ny) not in v and targetMap[nx][ny] != 1:
                        v.add((nx, ny))
                        q.append((nx, ny))
                        print(q, ret)

        return -1

    def isValid(self, m,n, x, y):
        if 0 <= x < m and 0 <= y < n:
            return True
        return False
