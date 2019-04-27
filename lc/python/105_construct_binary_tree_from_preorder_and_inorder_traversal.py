#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder.pop(0))
        node_index = inorder.index(node.val)
        
        node.left = self.buildTree(preorder, inorder[:node_index])
        node.right = self.buildTree(preorder, inorder[node_index+1:])
        
        return node

