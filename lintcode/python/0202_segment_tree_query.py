#!/usr/bin/python -t

# segment tree query

# beats 100%

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root.start == start and root.end == end:
            return root.max
            
        mid = (root.start+root.end)/2
        left, right = -sys.maxint, -sys.maxint
        #print root.start, root.end, mid
        #print start, end
        # left side
        if start <= mid:
            if mid < end:
                left = self.query(root.left, start, mid)
            else:
                left = self.query(root.left, start, end)
                
        # right side
        if mid < end:
            #print "right side ", start, end
            if start <= mid:
                right = self.query(root.right, mid+1, end)
            else:
                right = self.query(root.right, start, end)
                
        # or not within root start and end area.
        
        return max(left, right)
                

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root == None or start > end:
            return 0
            
        if start <= root.start and root.end <= end:
            return root.max
            
        return max(self.query(root.left, start, end),self.query(root.right, start, end))

