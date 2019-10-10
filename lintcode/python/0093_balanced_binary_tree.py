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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if root == None:
            return True
            
        balanced, _ = self.dfs(root)
        
        return balanced
        
    def dfs(self, node):
        if node == None:
            return True, 0
            
        l_b, l_d = self.dfs(node.left)
        if not l_b:
            return False, 0
            
        r_b, r_d = self.dfs(node.right)
        if not r_b:
            return False, 0
            
        return abs(l_d-r_d) <= 1, max(l_d, r_d)+1

