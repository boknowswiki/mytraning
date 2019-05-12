#!/usr/bin/python -t

class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.right)
        if not root.left:
            return
        self.flatten(root.left)
        tail = root.left
        while tail.right:
            tail = tail.right
        tail.right = root.right
        root.right = root.left
        root.left = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root


class Solution(object):
    # stack
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        current = root
        stack = [root]
        while stack:
            node = stack.pop()
            self.appendNode(stack, node.right)
            self.appendNode(stack, node.left)
            if current != node:
                current.right = node
                current.left = None
                current = node

    def appendNode(self, stack, node):
        if node:
            stack.append(node)
