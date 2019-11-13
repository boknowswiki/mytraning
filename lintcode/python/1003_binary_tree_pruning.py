#!/usr/bin/python -t

# dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
    """
    def pruneTree(self, root):
        # Write your code here
        if not root:
            return root
            
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and root.val == 0:
            return None
            
        return root
        
        
