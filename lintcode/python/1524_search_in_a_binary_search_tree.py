#!/usr/bin/python -t

# dfs, divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        if root == None:
            return None
            
        if root.val == val:
            return root
        elif root.val < val:
            ret = self.searchBST(root.right, val)
        else:
            ret = self.searchBST(root.left, val)
            
        return ret
     
