#!/usr/bin/python -t

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
