#!/usr/bin/python -t


class uf(object):
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
        self.size = [1] * n
        
        
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = self.father[qroot]
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = self.father[proot]
            self.size[proot] = self.size[proot] + self.size[qroot]
            
        return
        
    def find(self, p):
        tmp = p
        while p != self.father[p]:
            p = self.father[p]
        
        self.father[tmp] = p
        return p

    def better_find(self, p):
        if p != self.father[p]:
            self.father[p] = self.find(self.father[p]

        return self.father[p]
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution(object):
    def uftest(self, grid):
        """
        :type grid: List[int]
        :rtype: int
        """
        n = len(grid)
        myuf = uf(n)

        for i in range(1, n):
            myuf.union(grid[i], grid[i-1])

        return 0
        

if __name__ =='__main__':
    s = range(10)
    ss = Solution()
    print('answer is %d' % ss.uftest(s))

