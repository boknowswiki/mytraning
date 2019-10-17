#!/usr/bin/python -t

# dfs, traversal way
#从右子树开始递归，每次加上右子树的和，再递归左子树即可。

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
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.dfs(root)
        return root
        
    def dfs(self, node):
        if node == None:
            return
        
        if node.right:
            self.dfs(node.right)
            
        self.sum += node.val
        node.val = self.sum
        
        if node.left:
            self.dfs(node.left)
            

