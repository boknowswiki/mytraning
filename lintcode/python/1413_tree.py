#!/usr/bin/python -t

# hash table
# 一次dfs预处理出所有的信息，然后回答询问即可

class Solution:
    """
    @param x: The x
    @param y: The y
    @param a: The a
    @param b: The b
    @return: The Answer
    """
    def tree(self, x, y, a, b):
        # Write your code here
        n = len(x) + 1
        f = [0 for i in range(n + 1)]
        g = [[] for i in range(n + 1)]
        sons = [{} for i in range(n + 1)]
        for i in range(len(x)):
            print x[i], y[i]
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
            print g
            
        self.dfs(1, -1, g, f, sons)
        print g, f, sons
        
        ans = [0 for i in range(len(a))]
        for i in range(len(a)):
            if f[a[i]] == f[b[i]]:
                ans[i] = 1
            elif sons[a[i]].has_key(b[i]) or sons[b[i]].has_key(a[i]):
                ans[i] = 2
        return ans
        
    def dfs(self, rt, fa, g, f, sons):
        for x in g[rt]:
            if x == fa:
                continue
            f[x] = rt
            sons[rt][x] = x
            self.dfs(x, rt, g, f, sons)
            
