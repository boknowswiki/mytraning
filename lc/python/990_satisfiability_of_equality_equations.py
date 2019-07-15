#!/usr/bin/python -t

#union find solution

class uf(object):
    def __init__(self):
        self.father = {a:a for a in string.lowercase}
                
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        
        self.father[self.find(p)] = self.find(q)      
        
    def find(self, p):
        if self.father[p] != p:
            self.father[p] = self.find(self.father[p])
            
        return self.father[p]


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        myuf = uf()
        
        for a, e, _, b in equations:
            if e == '=':
                myuf.union(a, b)
        
        return not any(e == '!' and myuf.find(a) == myuf.find(b) for a, e, _, b in equations)

