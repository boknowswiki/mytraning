#!/usr/bin/python -t

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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        path = []
        
        self.dfs(root, target, 0, path, ret)
        
        return ret
        
    def dfs(self, node, target, level, path, ret):
        if node == None:
            return
        
        path.append(node.val)
        tmp = target
        
        for i in range(level, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                ret.append(path[i:])
                
        self.dfs(node.left, target, level+1, path, ret)
        self.dfs(node.right, target, level+1, path, ret)
        path.pop()
        
        return
    

