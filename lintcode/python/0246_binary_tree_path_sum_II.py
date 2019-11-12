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
    def __init__(self):
        
        self.results = []
    
    def binaryTreePathSum2(self, root, target):
        # write your code here
        if not root:
            return []
            
        self.traverse(root, target, [])
        self.binaryTreePathSum2(root.left, target)
        self.binaryTreePathSum2(root.right, target)
        
        return self.results
                
    def traverse(self, root, target, temp):
        
        if not root:
            return
        
        temp.append(root.val)
        
        if root.val == target:
            self.results.append(temp[:])
        if root.left:
            self.traverse(root.left, target - root.val, temp)
            temp.pop()
        
        if root.right:
            self.traverse(root.right, target - root.val, temp)
            temp.pop()
