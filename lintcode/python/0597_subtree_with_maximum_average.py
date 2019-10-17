#!/usr/bin/python -t

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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    
    def __init__(self):
        self.avg = 0
        self.node = None
        
    def findSubtree2(self, root):
        # write your code here
        if root == None:
            return self.node
            
        self.helper(root)
        
        return self.node
        
    def helper(self, node):
        if node == None:
            return 0, 0
            
        l_size, l_sum = self.helper(node.left)
        
        r_size, r_sum = self.helper(node.right)
        
        n_sum = (l_sum + r_sum + node.val)
        
        n_avg = (n_sum*1.0)/(l_size+r_size+1)
        
        if self.node == None or n_avg > self.avg:
            self.avg = n_avg
            self.node = node
            
        return (l_size+r_size+1), n_sum
