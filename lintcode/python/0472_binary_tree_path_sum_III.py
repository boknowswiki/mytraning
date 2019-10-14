#!/usr/bin/python -t

# dfs, traversal

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        ret = []
        self.dfs(root, target, ret)
        
        return ret
        
    def dfs(self, node, target, ret):
        if node == None:
            return
        
        self.findsum(node, None, target, [], ret)
        
        self.dfs(node.left, target, ret)
        self.dfs(node.right, target, ret)
        
    def findsum(self, node, father, target, path, ret):
        if node == None:
            return
        path.append(node.val)
        target -= node.val
        
        if target == 0:
            ret.append(path[:])
            
        if node.parent not in [None, father]:
            self.findsum(node.parent, node, target, path, ret)
        if node.left not in [None, father]:
            self.findsum(node.left, node, target, path, ret)
        if node.right not in [None, father]:
            self.findsum(node.right, node, target, path, ret)
            
        path.pop()
        
        return

