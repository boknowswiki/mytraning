#!/usr/bin/python -t

# dfs with divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        if root.left == None and root.right == None:
            #return ret.append(str(root.val))
            return [str(root.val)]
            
        l_paths = self.binaryTreePaths(root.left)
        r_paths = self.binaryTreePaths(root.right)
        
        for path in l_paths + r_paths:
            ret.append(str(root.val) + '->' + path)
            
        return ret

# dfs recursive traversal tree solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.helper(root, str(root.val), ret)
        
        return ret
    

    def helper(self, root, path, ret):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            ret.append(path)
            
        if root.left:
            self.helper(root.left, path + "->" + str(root.left.val), ret)
        if root.right:
            self.helper(root.right, path + "->" + str(root.right.val), ret)
            
        return

