#!/usr/bin/python -t

# segment tree build

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        n = len(A)
        
        return self.helper(A, 0, n-1)
        
        
    def helper(self, A, start, end):
        if start > end:
            return None
            
        if start == end:
            return SegmentTreeNode(start, end, A[start])
            
        node = SegmentTreeNode(start, end, A[start])
        
        mid = (start+end)/2
        node.left = self.helper(A, start, mid)
        node.right = self.helper(A, mid+1, end)
        node.max = max(node.left.max, node.right.max)
        
        return node

