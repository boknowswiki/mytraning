#!/usr/bin/python -t

# segment tree query II, solution 2

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root == None:
            return 0
            
        if root.start > end or root.end < start:
            return 0
            
        if root.start == root.end == start:
            return root.count
            
        if start == root.start and root.end == end:
            return root.count
        
        l_v = r_v = 0
        if root.left and start <= root.left.end:
            if end <= root.left.end:
                l_v = self.query(root.left, start, end)
            else:
                l_v = self.query(root.left, start, root.left.end)
                
        if root.right and end >= root.right.start:
            if start >= root.right.start:
                r_v = self.query(root.right, start, end)
            else:
                r_v = self.query(root.right, root.right.start, end)
                
        return l_v + r_v
            

# segment tree query II

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root == None:
            return 0
            
        if root.start > end or root.end < start:
            return 0
            
        if start <= root.start and root.end <= end:
            return root.count
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)

