#!/usr/bin/python -t


#union find solution

class uf(object):
    def __init__(self, m, n):
        self.father = []
        self.size = []
        for i in range(m):
            new_list = []
            for j in range(n):
                new_list.append((i, j))
            self.father.append(new_list)
            self.size.append([1]*n)
            
    def union(self, a, b):
        a = self.find(a[0], a[1])
        b = self.find(b[0], b[1])
        if self.size[a[0]][a[1]] < self.size[b[0]][b[1]]:
            self.father[a[0]][a[1]] = b
            self.size[b[0]][b[1]] += self.size[a[0]][a[1]]
        else:
            self.father[b[0]][b[1]] = a
            self.size[a[0]][a[1]] += self.size[b[0]][b[1]]
    
    def find(self, x, y):
        if self.father[x][y] == (x, y):
            return self.father[x][y]
        self.father[x][y] = self.find(self.father[x][y][0], self.father[x][y][1])
        return self.father[x][y]
        

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        myuf = uf(m, n)
        pos = {}
        
        for i in range(m):
            for j in range(n):
                pos[grid[i][j]] = (i, j)
                
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        for i in range(m*n):
            x, y = pos[i]
            for move in moves:
                xm = x + move[0]
                ym = y + move[1]
                if xm >= 0 and xm < m and ym >= 0 and ym < n:
                    if grid[xm][ym] <= i:
                        myuf.union((x, y), (xm, ym))
                    if myuf.find(0, 0) == myuf.find(m-1, n-1):
                        return i


if __name__ =='__main__':
    #s = [[0,2],[1,3]]
    s = [[6,22,3,23,1],[14,8,7,16,5],[11,0,9,15,18],[24,4,2,13,19],[20,10,17,21,12]]
    ss = Solution()
    print('answer is %d' % ss.swimInWater(s))

