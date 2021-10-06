#!/usr/bin/python -t

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return None

        if start == end:
            return SegmentTreeNode(start, start)
        
        root = SegmentTreeNode(start, end)
        root.left = self.build(start, (start+end)/2)
        root.right = self.build((start+end)/2+1, end)
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.build(1,4))