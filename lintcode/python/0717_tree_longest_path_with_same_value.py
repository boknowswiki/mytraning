#!/usr/bin/python -t

# bfs

import collections

class Solution:
    """
    @param A: as indicated in the description
    @param E: as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """
    def LongestPathWithSameValue(self, A, E):
        # write your code here
        n = len(A)
        tree = {}
        for i in range(n-1):
            x, y = E[2*i]-1, E[2*i+1]-1
            tree[x] = tree.get(x, []) + [y]
            tree[y] = tree.get(y, []) + [x]
            
        ret = [0]*n
        for i in range(n):
            q = collections.deque([[i, None, 0]])
            while q:
                node, par, step = q.popleft()
                ret[i] = max(ret[i], step)
                for nei in tree[node]:
                    if (nei != par or par is None) and A[nei] == A[node]:
                        q.append([nei, node, step+1])
                        
        return max(ret)


# dfs

class Solution:
    """
    @param A: as indicated in the description
    @param E: as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """
    def LongestPathWithSameValue(self, A, E):
        # write your code here
        n = len(A)
        graph = [[] for _ in range(n + 1)]
        for i in range(n - 1):
            graph[E[i * 2]].append(E[i * 2 + 1])
            graph[E[i * 2 + 1]].append(E[i * 2])
        A = [0] + A
        self.ans = 0
        temp = self.dfs(1, 0, A, graph)
        self.ans = max(temp, self.ans)
        return self.ans - 1
        
        
    def dfs(self, node, target, A, graph):
        v = []
        for e in graph[node]:
            if e != target:
                if A[e] == A[node]:
                    v.append(self.dfs(e, node, A, graph))
                else:
                    self.dfs(e, node, A, graph)
                    
        #print v
        v.append(0)
        v.append(0)
        #print v
        v.sort()
        v.reverse()
        self.ans = max(self.ans, v[0] + v[1] + 1)
        return v[0] + 1
        
