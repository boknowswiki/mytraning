#!/usr/bin/python -t

# bfs and spfa

#这个题目想清楚是SPFA了以后巨简单。 一个让code变优雅的办法是不要额外记录step， 而是直接visited map到step。 然后可以游到的step， 应该是上一个格子可以游到的， 或者是水位。
#
#还有个变优雅的方法是， init的时候， 取一个很大的值， 这样就不需要特殊判断之前有没有到过这个点了。

import collections

class Solution:
    """
    @param grid: the grid
    @return: the least time you can reach the bottom right square
    """
    def swimInWater(self, grid):
        # Write your code here
        v = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        q = collections.deque([(0, 0)])
        v[0][0] = grid[0][0]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            step = v[x][y]
            for i in range(len(dirs)):
                nx = x + dirs[i][0]
                ny = y + dirs[i][1]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if v[nx][ny] <= step:
                    continue
                v[nx][ny] = max(step, grid[nx][ny])
                q.append((nx, ny))

        return v[len(grid)-1][len(grid[0])-1]




if __name__ == '__main__':
    s = Solution()
    a = [[0,2],[1,3]]
    print(s.swimInWater(a))