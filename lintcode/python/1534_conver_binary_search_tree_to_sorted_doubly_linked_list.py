#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        self.head, self.last = None, None
        
        self.inoder(root)
        
        self.head.left = self.last
        self.last.right = self.head
        
        return self.head
        
    def inoder(self, node):
        if not node:
            return
        
        self.inoder(node.left)
        
        if not self.head:
            self.head = node
            self.last = node
        else:
            self.last.right = node
            node.left = self.last
            self.last = node
        
        self.inoder(node.right)
        
        return
