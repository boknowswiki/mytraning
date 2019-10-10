#!/usr/bin/python -t

# pure divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        min_val, subtree_node, total = self.dfs(root)
        
        return subtree_node
        
    def dfs(self, node):
        if node == None:
            return sys.maxint, None, 0
        
        leftmin, l_node, left_total = self.dfs(node.left)
        rightmin, r_node, right_total = self.dfs(node.right)
        
        total = left_total+right_total+node.val
        
        if leftmin == min(leftmin, rightmin, total):
            return leftmin, l_node, total
        if rightmin == min(leftmin, rightmin, total):
            return rightmin, r_node, total
            
        return total, node, total

# divid and conquer with golbal state

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    
    def __init__(self):
        self.min_sum = sys.maxint
        self.ret_node = None
    def findSubtree(self, root):
        # write your code here
        self.dfs(root)
        
        return self.ret_node
        
    def dfs(self, node):
        if node == None:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        total = left+right+node.val
        
        if total < self.min_sum:
            self.min_sum = total
            self.ret_node = node
            
        return total

