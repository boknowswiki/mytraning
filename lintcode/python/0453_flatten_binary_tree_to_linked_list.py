#!/usr/bin/python -t

# bfs non-recursive way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        
        s = [root]
        
        while len(s) != 0:
            node = s.pop()
            
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
                
            node.left = None
            if len(s) == 0:
                node.right = None
            else:
                node.right = s[-1]
                
        return


# dfs traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def __init__(self):
        self.lastnode = None
        
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        
        if self.lastnode != None:
            self.lastnode.right = root
            self.lastnode.left = None
            
        self.lastnode = root
        rightnode = root.right
        self.flatten(root.left)
        self.flatten(rightnode)
        
        return
    

# pure divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        
        self.helper(root)
        
        return
    
    def helper(self, node):
        if node == None:
            return
        
        l_last = self.helper(node.left)
        r_last = self.helper(node.right)
        
        if l_last != None:
            l_last.right = node.right
            node.right = node.left
            node.left = None
            
        if r_last != None:
            return r_last
            
        if l_last != None:
            return l_last
            
        return node
        

