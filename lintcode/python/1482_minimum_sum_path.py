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
    @param root: the root
    @return: minimum sum
    """
    def minimumSum(self, root):
        # Write your code here
        if root == None:
            return 0
            
        min_val = self.dfs(root)
        
        return min_val
        
    def dfs(self, node):
        if node.left == None and node.right == None:
            return node.val
            
        if node.left != None and node.right != None:
            return node.val + min(self.dfs(node.left), self.dfs(node.right))
        elif node.left != None:
            return node.val + self.dfs(node.left)
        else:
            return node.val + self.dfs(node.right)

