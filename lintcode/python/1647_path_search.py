#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param n: The number of points
    @param G: The description of graph
    @param S: The point S
    @param T: The point T
    @return: output all the paths from S to T
    """
    def getPath(self, n, G, S, T):
        # Write your code here
        ret = []
        path = []
        
        edge = []
        v = set()
        
        for i in range(n):
            edge.append([])
            
        m = len(G)
        for i in range(m):
            x = G[i][0]
            y = G[i][1]
            edge[x].append(y)
            edge[y].append(x)
            
        for i in range(n):
            edge[i].sort()
            
        v.add(S)
        path.append(S)
        self.dfs(S, T, path, ret, edge, v)
        
        return ret
        
    def dfs(self, cur, target, path, ret, edge, v):
        if cur == target:
            ret.append(list(path))
            
        #v.add(cur)
        #path.append(cur)
        for nxt in edge[cur]:
            if nxt not in v:
                v.add(nxt)
                path.append(nxt)
                self.dfs(nxt, target, path, ret, edge, v)
                path.pop()
                v.remove(nxt)
                
        return
    
    
            
