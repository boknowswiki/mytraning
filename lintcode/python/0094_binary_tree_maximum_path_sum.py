#!/usr/bin/python -t

# dp solution time O(n) space O(1)

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
    def maxPathSum(self, root):
        # write your code here
        # singlePath: 从root往下走到任意点的最大路径，这条路径可以不包含任何点
        # maxPath: 从树中任意到任意点的最大路径，这条路径至少包含一个点
        max_val, single_val = self.helper(root)
        
        return max_val
        
    def helper(self, root):
        if root == None:
            return -sys.maxint-1, 0
        
        left_max, left_single = self.helper(root.left)
        right_max, right_single = self.helper(root.right)
        
        single_val = max(left_single, right_single) + root.val
        single_val = max(single_val, 0)
        
        max_val = max(left_max, right_max)
        max_val = max(max_val, left_single + right_single + root.val)
        
        return max_val, single_val

