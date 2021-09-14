#!/usr/bin/python -t

# bfs

from typing import (
    List,
)

import collections

class Solution:
    """
    @param mazeMap: a 2D grid
    @return: return the minium distance
    """
    def getMinDistance(self, mazeMap: List[List[int]]) -> int:
        # write your code here
        m = len(mazeMap)
        if m == 0:
            return 0

        n = len(mazeMap[0])

        d = collections.defaultdict(list)

        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if mazeMap[i][j] == -2:
                    start = (i, j)
                elif mazeMap[i][j] == -3:
                    end = (i, j)
                elif mazeMap[i][j] > 0:
                    d[mazeMap[i][j]].append((i, j))

        q = collections.deque([start])
        v = set()
        v.add(start)

        while q:
            l = len(q)
            ret += 1
            for _ in range(l):
                x, y = q.popleft()
                if mazeMap[x][y] > 0:
                    for nx, ny in d[mazeMap[x][y]]:
                        if (nx, ny) == end:
                            return ret
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v and mazeMap[nx][ny] != -1:
                            q.append((nx, ny))
                            v.add((nx, ny))
                    del d[mazeMap[x][y]]
                        
                for i in range(len(dirs)):
                    nx = x + dirs[i][0]
                    ny = y + dirs[i][1]
                    if (nx, ny) == end:
                        return ret
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v and mazeMap[nx][ny] != -1:
                        q.append((nx, ny))
                        v.add((nx, ny))

        return -1
