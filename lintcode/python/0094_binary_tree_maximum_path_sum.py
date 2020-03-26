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


# divid and conqur

# left_ret is max for all left side subtree
# left_left and left_right is left node's left and right nodes max values
# right_ret is max for all right side subtree
# right_left and right_right is right node's left and right nodes max values

# for parent node, the left and right need to get max for
# left = max(left_left+node.left.val, left_right+node.left.val, node.left.val)
# right = max(right_left+node.right.val, right_right+node.right.val, node.right.val)
# for max value, could be left_ret, right_ret or left+node.val, right+node.val, left+node.val+right, node.val
# max = max(left+node.val, right+node.val, node.val, left+node.val+right, left_ret, right_ret)


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
        if not root:
            return 0
            
        ret, left, right = self.dfs(root)
        
        return ret
        
    def dfs(self, node):
        if not node:
            return -sys.maxint, -sys.maxint, -sys.maxint
            
        left_ret, left_left, left_right = self.dfs(node.left)
        right_ret, right_left, right_right = self.dfs(node.right)
        
        left = 0
        right = 0
        
        if node.left:
            left = max(left_left+node.left.val, left_right+node.left.val, node.left.val)
        if node.right:
            right = max(right_left+node.right.val, right_right+node.right.val, node.right.val)
            
        ret = 0
        
        ret = max(left+node.val, right+node.val, node.val, left+node.val+right, left_ret, right_ret)
        

        return ret, left, right
        
