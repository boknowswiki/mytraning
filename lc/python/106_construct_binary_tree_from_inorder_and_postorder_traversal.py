#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        node = TreeNode(postorder.pop())
        node_index = inorder.index(node.val)
        
        node.right = self.buildTree(inorder[node_index+1:], postorder)
        node.left = self.buildTree(inorder[:node_index], postorder)
        
        return node

