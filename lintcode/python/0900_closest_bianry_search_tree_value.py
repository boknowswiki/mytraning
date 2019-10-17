#!/usr/bin/python -t

# iteration way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root == None:
            return None
            
        lower = upper = root
        
        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root
                
        if abs(target - lower.val) < abs(upper.val - target):
            return lower.val
        return upper.val
        

# dfs, lower and upper bound

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root == None:
            return None
        
        low = self.lower(root, target)
        up = self.upper(root, target)
        
        if low == None:
            return up.val
            
        if up == None:
            return low.val
            
        if target-low.val < up.val-target:
            return low.val
        return up.val
            
    def lower(self, node, target):
        if node == None:
            return None
        
        if node.val > target:
            return self.lower(node.left, target)
        
        low = self.lower(node.right, target)
        
        return node if low is None else low
        
    def upper(self, node, target):
        if node == None:
            return None
            
        if node.val <= target:
            return self.upper(node.right, target)
            
        up = self.upper(node.left, target)
        
        return node if up is None else up
        
            
