#!/usr/bin/python -t

# dfs, divid and conquer with traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def addOneRow(self, root, v, d):
        # write your code here
        if not root:
            return None
            
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
            
        if d == 2:
            l_node = TreeNode(v)
            r_node = TreeNode(v)
            root.left, l_node.left = l_node, root.left
            root.right, r_node.right = r_node, root.right
            return root
            
        elif d > 2:
            root.left = self.addOneRow(root.left, v, d-1)
            root.right = self.addOneRow(root.right, v, d-1)
        return root
        
