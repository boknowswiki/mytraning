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
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        # write your code here
        if not root:
            return 0
            
        self.ret = 0
        
        self.dfs(root, root.val)
        
        return self.ret
        
    def dfs(self, node, val):
        if node.left == None and node.right == None:
            self.ret += val
            
        if node.left:
            self.dfs(node.left, val*10+node.left.val)
        if node.right:
            self.dfs(node.right, val*10+node.right.val)
            
        return
