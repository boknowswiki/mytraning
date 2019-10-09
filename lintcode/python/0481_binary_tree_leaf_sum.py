#!/usr/bin/python -t

# divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        if root == None:
            return 0
            
        if root.left == None and root.right == None:
            return root.val
            
        l = self.leafSum(root.left)
        r = self.leafSum(root.right)
        
        return l+r

# dfs tree traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    
    def __init__(self):
        self.ret = 0
        
    def leafSum(self, root):
        # write your code here
        if root == None:
            return self.ret
        
        if root.left == None and root.right == None:
            self.ret += root.val
            
        self.leafSum(root.left)
        self.leafSum(root.right)
        
        return self.ret

