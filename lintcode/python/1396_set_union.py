#!/usr/bin/python -t

# union find

class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        n = len(sets)
        dsu = DSU(n)
        setMap = {}
        for i in range(len(sets)):
            set = sets[i]
            for j in range(len(set)):
                if set[j] in setMap:
                    dsu.union(i, setMap[set[j]])
                else:
                    setMap[set[j]] = i
        return dsu.count

class DSU:
    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.size = [1 for i in range(length)]
        self.count = length

    def find(self, point):
        if point != self.parent[point]:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]

    def union(self, point1, point2):
        root1 = self.find(point1)
        root2 = self.find(point2)
        if root1 == root2:
            return
        if self.size[root1] <= self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        self.count -= 1
