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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
            
        cur = root
        
        while cur != node:
            if cur.val < node.val:
                if cur.right == None:
                    cur.right = node
                cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                cur = cur.left
                
        return root
        

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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
            
        if node.val < root.val:
            if root.left:
                self.insertNode(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                self.insertNode(root.right, node)
            else:
                root.right = node
                
        return root

