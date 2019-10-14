#!/usr/bin/python -t

# iteration way

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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root == None:
            return True
            
        s = []
        
        while root:
            s.append(root)
            root = root.left
            
        lastnode = s[-1]
        while len(s) > 0:
            node = s.pop()
            if node.right:
                node = node.right
                while node:
                    s.append(node)
                    node = node.left
                    
            if len(s) > 0:
                if s[-1].val <= lastnode.val:
                    return False
                lastnode = s[-1]
                
        return True
        


# dfs,  divid and conquer solution

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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        isBST, min_val, max_val = self.dfs(root)
        
        return isBST
        
    def dfs(self, node):
        if node == None:
            return True, None, None
            
        l_isBST, l_min, l_max = self.dfs(node.left)
        r_isBST, r_min, r_max = self.dfs(node.right)
        
        if not l_isBST or not r_isBST:
            return False, None, None
            
        if l_max is not None and l_max >= node.val:
            return False, None, None
        if r_min is not None and r_min <= node.val:
            return False, None, None
            
        min_val = l_min if l_min is not None else node.val
        max_val = r_max if r_max is not None else node.val
        
        return True, min_val, max_val
        


# dfs, traversal way

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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.isBST = True
        self.lastval = None
        
        self.valid(root)
        
        return self.isBST
        
    def valid(self, node):
        if node == None:
            return
        
        self.valid(node.left)
        
        if self.lastval != None and self.lastval >= node.val:
            self.isBST = False
            return
        
        self.lastval = node.val
        self.valid(node.right)
        
        return
    
