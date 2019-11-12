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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
            
        return self.dfs(root)
           
    def dfs(self, root):
        if not root:
            return sys.maxint
            
        if not root.left and not root.right:
            return 1
        
        min_left = self.dfs(root.left)
        min_right = self.dfs(root.right)
        
        return min(min_left, min_right) + 1

