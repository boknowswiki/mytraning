#!/usr/bin/python -t

# dfs and divid and conquer

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def __init__(self):
        self.max_val = -sys.maxint
        self.ret_node = None
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root:
            return root
            
        self.dfs(root)
        
        return self.ret_node
        
    def dfs(self, node):
        if not node:
            return 0
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        total = node.val + l + r
        if total > self.max_val:
            self.max_val = total
            self.ret_node = node
            
        return total
        
