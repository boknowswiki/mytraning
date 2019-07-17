#!/usr/bin/python -t

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

