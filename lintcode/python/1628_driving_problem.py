#!/usr/bin/python -t

# 并查集，如果有障碍物，小车从障碍物上面下面或者两个障碍物之间过去，判断是哪种情况，根据每种不同的情况，判断图如何连通，如果三种情况都无法通过，即小车走不到终点

class Solution:
    """
    @param L: the length
    @param W: the width
    @param p:  the obstacle coordinates
    @return: yes or no
    """
    def drivingProblem(self, L, W, p):
        # Write your code here.
        n = len(p)
        self.parent = [i for i in range(n+2)]
        #print self.parent
        self.size = [1] * (n+2)
        for i in range(n):
            for j in range(i+1, n):
                #print i, p[i], j, p[j]
                dx, dy = p[i][0] - p[j][0],  p[i][1] - p[j][1]
                if dx * dx + dy * dy <= 36:
                    #print i, j
                    self.union(i, j)
                    #print self.parent
            
            if p[i][1] <= 5:
                #print i, n
                self.union(i, n) 
                #print self.parent
            
            if W - p[i][1] <= 5:
                #print i, n+1
                self.union(i, n+1)
                #print self.parent
                
        print self.parent
        return 'yes' if self.union(n, n+1) else 'no'
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return False
        if self.size[i] > self.size[j]:
            self.parent[j] = i
            self.size[i] += self.size[j]
        else:
            self.parent[i] = j
            self.size[j] += self.size[i]
        return True
