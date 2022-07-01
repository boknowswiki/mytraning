#!/usr/bin/python -t


# dfs, divid and conquer way
# time O(n)
# space O(1)

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        if not root:
            return 0

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

# dfs, traversal solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    
    def __init__(self):
        self.ret = 0
        
    def maxDepth(self, root):
        # write your code here
        self.dfs(root, 1)
        
        return self.ret
        
    def dfs(self, node, dep):
        if node == None:
            return
        
        if dep > self.ret:
            self.ret = dep
            
        self.dfs(node.left, dep+1)
        self.dfs(node.right, dep+1)
        
        return

# dfs, divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root == None:
            return 0
            
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

