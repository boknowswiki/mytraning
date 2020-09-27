#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None
    """
    @param root: the given tree
    @return: the tree after swapping
    """
    def bstSwappedNode(self, root):
        # write your code here
        if not root:
            return root
            
        self.dfs(root)
        
        if self.first != None:
            self.first.val, self.second.val = self.second.val, self.first.val
            
        return root
        
    def dfs(self, node):
        if node == None:
            return
        
        self.dfs(node.left)
        
        if self.pre != None:
            if self.pre.val > node.val:
                if self.first == None:
                    self.first = self.pre
                self.second = node
            
        self.pre = node
        
        self.dfs(node.right)
        
        return
    
