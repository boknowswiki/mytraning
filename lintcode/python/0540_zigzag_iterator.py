#!/usr/bin/python -t

class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        if self.index1 >= len(self.v1):
            val = self.v2[self.index2]
            self.index2 += 1
            return val
        if self.index2 >= len(self.v2):
            val = self.v1[self.index1]
            self.index1 += 1
            return val
        if self.index1 == self.index2:
            val = self.v1[self.index1]
            self.index1 += 1
            return val
        else:
            val = self.v2[self.index2]
            self.index2 += 1
            return val
            

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        if self.index1 >= len(self.v1) and self.index2 >= len(self.v2):
            return False
        return True


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
