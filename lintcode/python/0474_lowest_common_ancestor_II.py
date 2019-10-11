#!/usr/bin/python -t

# LCA solution

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        d = {}
        
        while A != root:
            d[A] = True
            A = A.parent
            
        while B != root:
            if B in d:
                return B
            B = B.parent
            
        return root

