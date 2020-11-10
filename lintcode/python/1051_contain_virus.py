#!/usr/bin/python -t

#直接模拟即可。
#
#在每一天开始的时候，通过dfs找出所有被感染了并且没有被墙围住的区域（联通分量），dfs的同时计算出围住该区域所需要的墙的数量，以及和即将被该区域感染的cell的集合。
#找出所有区域之后，选取即将要感染最多格子的那个区域，并将该区域内部所有格子标记为2,表示已经被墙包围，同时将其边界长度加入最后的答案中;
#对于剩余的区域，则把其待感染的格子标记为1,表示已被感染。
#循环上述过程，直至所有病毒被墙包围或者所有格子都被感染。

class Solution:
    """
    @param grid: the given 2-D world
    @return: the number of walls
    """
    def containVirus(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def getgroups():
            groups = []
            visited = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j]!=1 or (i, j) in visited:
                        continue
                    group = set()
                    q = [(i, j)]
                    while q:
                        (x, y) = q.pop(0)
                        visited.add((x, y))
                        group.add((x, y))
                        for (dx, dy) in ds:
                            xx, yy = x+dx, y+dy
                            if 0<=xx<m and 0<=yy<n and grid[xx][yy]==1 and (xx, yy) not in visited:
                                visited.add((xx, yy))
                                q.append((xx, yy))
                    groups.append(group)
            return groups
                
        def expand(group):
            ret = collections.Counter()
            for (i, j) in group:
                for (dx, dy) in ds:
                    xx, yy = i+dx, j+dy
                    if 0<=xx<m and 0<=yy<n and grid[xx][yy]==0:
                        ret[(xx, yy)] += 1
            return ret
              
        groups = getgroups()
        nwalls = 0


            
        while groups:
            if sum(len(g) for g in groups)==m*n:
                return nwalls
            walls = [expand(g) for g in groups]
            
            maxi = -1
            maxunaff = 0
        
            for i in range(len(walls)):
                tmp = len(walls[i])
                if tmp>maxunaff:
                    maxi, maxunaff = i, tmp
            
            #print([len(wall) for wall in walls])
            for (x, y) in groups[maxi]:
                grid[x][y] = 2
            
            # for _ in range(m):
            #     print(grid[_])
            # print("Build wall for group {}/{}".format(maxi, len(groups)))
            nwalls += sum(walls[maxi].values())
            walls = walls[:maxi]+walls[maxi+1:]
            for wall in walls:
                for (x, y) in wall:
                    grid[x][y] = 1
            # for _ in range(m):
            #     print(grid[_])
            # print(nwalls)
            groups = getgroups()
        
        return nwalls
