#!/usr/bin/python -t

#union find

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [0] * (n+1)

        for i in range(1, n+1):
            self.father[i] = i
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        if self.father[a] == self.father[b]:
            return
        
        self.father[self.find(a)] = self.find(b)
        
        return

    def find(self, a):
        if self.father[a] == a:
            return a
            
        self.father[a] = self.find(self.father[a])
        return self.father[a]
        
    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)

