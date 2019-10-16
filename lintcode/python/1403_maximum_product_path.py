#!/usr/bin/python -t

# dfs and graph

class Solution:
    """
    @param x: The end points of edges set
    @param y: The end points of edges set
    @param d: The weight of points set
    @return: Return the maximum product
    """
    ans = 0
    def dfs(self, x, f, g, d, mul):
        isLeaf = True
        mod = 1000000007
        mul = mul * d[x - 1] % mod
        for i in g[x]:
            if i == f:
                continue
            isLeaf = False
            self.dfs(i, x, g, d, mul)
        if(isLeaf is True):
            self.ans = max(self.ans, mul)
    def getProduct(self, x, y, d):
        # Write your code here
        n = len(d)
        g = [ [] for i in range(n + 1)]
        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
        self.dfs(1, -1, g, d, 1)
        return self.ans
        
