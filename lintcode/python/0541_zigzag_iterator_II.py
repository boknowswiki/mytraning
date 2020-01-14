#!/usr/bin/python -t

class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.q = [v for v in vecs if v]
    """
    @return: An integer
    """
    def next(self):
        # write your code here
        v = self.q.pop(0)
        val = v.pop(0)
        if v:
            self.q.append(v)
            
        return val
        

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.q) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result

