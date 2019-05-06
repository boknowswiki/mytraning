#!/usr/bin/python -t

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        s = [root]
        
        while s:
            node = s.pop()
            node.left, node.right = node.right, node.left
            
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
                
        return root

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        if root == None:
            return root
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        
        return root


