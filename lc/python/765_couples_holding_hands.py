#!/usr/bin/python -t

class uf(object):
    def __init__(self, n):
        self.father = {a:a for a in range(n)}
        self.cnt = n
        print self.father
                
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        
        self.father[self.find(p)] = self.find(q)     
        self.cnt = self.cnt - 1
        
    def find(self, p):
        print p, self.father
        if self.father[p] != p:
            self.father[p] = self.find(self.father[p])
            
        return self.father[p]

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        n = n//2
        myuf = uf(n)
        
        for i in range(n):
            a = row[2*i]
            b = row[2*i+1]
            myuf.union(a/2, b/2)
            
        return n - myuf.cnt

if __name__ =='__main__':
    s = [0,2,1,3]
    ss = Solution()
    print('answer is %d' % ss.minSwapsCouples(s))
