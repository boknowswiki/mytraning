#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        pre = None
        while root:
            #print root.val, p.val
            if root.val >= p.val:
                root = root.left
            else:
                if pre == None or root.val > pre.val:
                    pre = root
                root = root.right
                
        return pre
