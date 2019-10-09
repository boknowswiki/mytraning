#!/usr/bin/python -t

# recursive traversal solution

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
    @return: Postorder in ArrayList which contains node values.
    """
    def __init__(self):
        self.ret = []
        
    def postorderTraversal(self, root):
        # write your code here
        self.traverse(root)
        
        return self.ret
        
    def traverse(self, node):
        if node == None:
            return
        
        self.traverse(node.left)
        self.traverse(node.right)
        self.ret.append(node.val)
        
        return
    

