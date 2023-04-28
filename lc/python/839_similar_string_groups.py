#!/usr/bin/python -t

# bfs
# time O(n^2*m)
# space O(n^2)

import collections

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        graph = collections.defaultdict(list)

        def is_similar(a, b):
            diff = 0
            for i, j in zip(a, b):
                if i != j:
                    diff += 1

            return diff == 0 or diff == 2

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        v = set()
        cnt = 0

        def bfs(idx):
            nonlocal graph, v, strs
            q = collections.deque([idx])
            v.add(idx)

            while q:
                cur = q.popleft()
                if cur not in graph:
                    continue
                
                for nei in graph[cur]:
                    if nei not in v:
                        v.add(nei)
                        q.append(nei)

            return

        for i in range(len(strs)):
            if i not in v:
                bfs(i)
                cnt += 1

        return cnt

#union find solution, but time limit exceeded, but it's right.

class uf(object):
    def __init__(self, n):
        self.father = range(n)
        self.cnt = n
        
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        self.father[proot] = qroot
            
        self.cnt -= 1
            
    def find(self, p):
        if p != self.father[p]:
            self.father[p] = self.find(self.father[p])
            
        return self.father[p]
    
    def get_num_groups(self):
        return sum([1 for i in range(len(self.father)) if i == self.father[i]])

class Solution(object):
    def is_similar(self, a, b):
        return len(list(filter(lambda i: a[i] != b[i], range(len(a))))) in (0, 2)
    
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def is_similar(s, ss):
            sn = len(s)
            dn = 0
            
            for i in range(sn):
                if s[i] != ss[i]:
                    dn = dn+1
                    if dn > 2:
                        return False
            return True
        
        n = len(A)
        
        myuf = uf(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if self.is_similar(A[i], A[j]):
                    myuf.union(i, j)
                    
        return myuf.cnt
        #return myuf.get_num_groups()

