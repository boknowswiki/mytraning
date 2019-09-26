#!/usr/bin/python -t

# segment tree and binary search
# build O(n) query O(logn), space O(n)

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class sgtree(object):
    def __init__(self, start, end, s_val=0):
        self.start = start
        self.end = end
        self.s_val = s_val
        self.left, self.right = None, None
        
    @classmethod
    def build(cls, start, end, s):
        if start > end:
            return None
        if start == end:
            return sgtree(start, end, s[start])
        
        node = sgtree(start, end, s[start])
        mid = (start+end)/2
        node.left = cls.build(start, mid, s)
        node.right = cls.build(mid+1, end, s)
        node.s_val = node.left.s_val + node.right.s_val
        
        return node
        
    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
            
        if start <= root.start and root.end <= end:
            return root.s_val
            
        return (cls.query(root.left, start, end)+cls.query(root.right, start, end))
        

class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        root = sgtree.build(0, len(A)-1, A)
        ret = []
        for q in queries:
            ret.append(sgtree.query(root, q.start, q.end))
            
        return ret

