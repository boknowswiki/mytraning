#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []
            
        self.h = {}
        self.ret = []
        self.dfs(root)
        
        return self.ret
        
    def dfs(self, node):
        if node == None:
            return "#"
            
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        node_str = left + str(node.val) + right
        
        self.h[node_str] = self.h.get(node_str, 0) + 1
        
        if self.h[node_str] == 2:
            self.ret.append(node)
        
        return node_str
