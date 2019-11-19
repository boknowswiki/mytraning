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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        if not root:
            return 0
            
        ret, _, _ = self.dfs(root)
        
        return ret
        
    def dfs(self, node):
        if node == None:
            return 0, 0, 0
            
        
            
        left, left_down, left_up = self.dfs(node.left)
        right, right_down, right_up = self.dfs(node.right)
        
        down, up = 0, 0
        
        if node.left and node.left.val + 1 == node.val:
            down = max(down, left_down+1)
        if node.left and node.left.val - 1 == node.val:
            up = max(up, left_up+1)
        if node.right and node.right.val + 1 == node.val:
            down = max(down, right_down+1)
        if node.right and node.right.val - 1 == node.val:
            up = max(up, right_up+1)
            
        ret = down + 1 + up
        ret = max(ret, left, right)
        
        return ret, down, up
        
        
