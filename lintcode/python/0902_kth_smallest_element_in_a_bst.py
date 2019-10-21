#!/usr/bin/python -t

# bfs, inorder traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        index = 0
        s = []
        
        while root:
            s.append(root)
            root = root.left
            
        while s:
            node = s.pop()
            index += 1
            if index == k:
                return node.val
            if node.right:
                node = node.right
                while node:
                    s.append(node)
                    node = node.left
                    
        return s[-1].val

# dfs traversal bst

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.ret = None
        self.index = 0
        
        self.inorder(root, k)
        
        return self.ret
        
    def inorder(self, node, k):
        if node == None:
            return 
        
        self.inorder(node.left, k)
        self.index += 1
        
        if self.index == k:
            self.ret = node.val
            return
        
        self.inorder(node.right, k)
        
        return
    
