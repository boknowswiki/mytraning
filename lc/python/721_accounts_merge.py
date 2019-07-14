#!/usr/bin/python -t

#union find solution

class uf(object):
    def __init__(self,):
        self.father = range(10001)
                
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
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        myuf = uf()
        em_to_name = {}
        em_to_id = {}
        i = 0
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i = i + 1
                    
                myuf.union(em_to_id[acc[1]], em_to_id[email])
                
        ans = collections.defaultdict(list)
        
        for email in em_to_name:
            ans[myuf.find(em_to_id[email])].append(email)
            
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

