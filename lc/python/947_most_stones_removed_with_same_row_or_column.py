#!/usr/bin/python -t

# union find
# time O(n)
# space O(n)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def find(x):
            while x != parent.setdefault(x, x):
                x = find(parent[x])
            #print(f"find x {x}")
            return x
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            #print(f"union x {x}, {root_x}, y {y}, {root_y}")
            if root_x != root_y:
                parent[root_x] = root_y
        
        # a stone's row and col is connected by default
        # use ~ to make negative value to distinguish col with row number
        for i, j in stones:
            #print(f" i {i}, j {j}")
            union(i, ~j)
        
        #print(parent)
        #print(set(find(x) for x in parent))
        return len(stones) - len(set(find(x) for x in parent))
        

class uf(object):
    def __init__(self, n):
        self.father = range(n)
        self.size = [1] * n
        
    def find(self, p):
        tmp = p
        
        while p != self.father[p]:
            p = self.father[p]
            
        self.father[tmp] = p
        
        return p
    
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = qroot
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = proot
            self.size[proot] = self.size[proot] + self.size[qroot]
            
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        myuf = uf(20000)
        
        for p, q in stones:
            myuf.union(p, q+10000)
                
        c = [myuf.find(p) for p, q in stones]
        d = {myuf.find(p) for p, q in stones}
        
        #return n - len(set(c))
        return n - len(d)

