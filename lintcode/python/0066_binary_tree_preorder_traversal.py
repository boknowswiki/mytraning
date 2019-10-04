#!/usr/bin/python -t

# binary tree traversal, recursive way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.helper(root, ret)
        
        return ret
        
    def helper(self, root, ret):
        if root == None:
            return
        ret.append(root.val)
        self.helper(root.left, ret)
        self.helper(root.right, ret)
        
        return

