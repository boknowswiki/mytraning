#!/usr/bin/python -t

# union find

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [0] * (1+n)
        for i in range(1, n+1):
            self.father[i] = i
        
        self.size = [1] * (1+n)

    def find(self, a):
        #print self.father, a
        if self.father[a] == a:
            return a
        
        return self.find(self.father[a])
        
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        #print a, b
        roota = self.find(a)
        #print roota
        rootb = self.find(b)
        #print roota, rootb
        if roota == rootb:
            return
        
        self.father[roota] = rootb
        self.size[rootb] = self.size[roota]+self.size[rootb]
        #print self.father
        #print self.size
        return
        

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.size[self.find(a)]
