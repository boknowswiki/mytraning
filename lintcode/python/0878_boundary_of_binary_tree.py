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
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        self.ret = []
        
        if not root:
            return self.ret
            
        self.ret.append(root.val)
        
        if root.left == None and root.right == None:
            return self.ret
        
        self.dfsleft(root.left)
        self.dfsleaf(root)
        self.dfsright(root.right)
        
        return self.ret
        
        
    def dfsleft(self, node):
        if not node or (node.left == None and node.right == None):
            return
        
        self.ret.append(node.val)
        
        if node.left:
            self.dfsleft(node.left)
        else:
            self.dfsleft(node.right)
        
        return
    
    def dfsleaf(self, node):
        if not node:
            return
        
        if node.left == None and node.right == None:
            self.ret.append(node.val)
            return
        
        self.dfsleaf(node.left)
        self.dfsleaf(node.right)
            
        return
    
    def dfsright(self, node):
        if not node or (node.left == None and node.right == None):
            return
        
        if node.right:
            self.dfsright(node.right)
        else:
            self.dfsright(node.left)
        
        self.ret.append(node.val)
        
        return
    
