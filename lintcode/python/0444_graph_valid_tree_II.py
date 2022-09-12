#!/usr/bin/python -t

# union find
# time O(n)
# space O(n)

class Solution:
    def __init__(self):
        self.father = {}
        self.edges = 0
        self.node = 0
        self.has_circle = False

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])

        return self.father[x]


    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.father[a_root] = b_root
        else:
            self.has_circle = True

        return

    """
    @param a: the node a
    @param b: the node b
    @return: nothing
    """
    def addEdge(self, a, b):
        # write your code here
        if a not in self.father:
            self.father[a] = a
            self.node += 1
        if b not in self.father:
            self.father[b] = b
            self.node += 1

        self.union(a, b)
        self.edges += 1

        return


    """
    @return: check whether these edges make up a valid tree
    """
    def isValidTree(self):
        # write your code here
        if self.node == self.edges + 1 and self.has_circle == False:
            return True
        return False
