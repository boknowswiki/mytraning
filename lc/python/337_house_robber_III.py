#!/usr/bin/python -t

# dfs/dp solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0,0)
            l, r = dfs(node.left), dfs(node.right)
            return (max(l)+max(r), node.val+l[0]+r[0])
        
        return max(dfs(root))

