#!/usr/bin/python -t

# binary tree
# divid and conquer way
# time O(n)
# space O(1)


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        if not root:
            return True

        balanced, _ = self.helper(root)

        return balanced

    def helper(self, node):
        if not node:
            return True, 0

        l_b, l_d = self.helper(node.left)
        r_b, r_d = self.helper(node.right)

        balanced = l_b and r_b and abs(l_d -r_d) < 2
        depth = max(l_d, r_d) + 1

        return balanced, depth

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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if root == None:
            return True
            
        balanced, _ = self.dfs(root)
        
        return balanced
        
    def dfs(self, node):
        if node == None:
            return True, 0
            
        l_b, l_d = self.dfs(node.left)
        if not l_b:
            return False, 0
            
        r_b, r_d = self.dfs(node.right)
        if not r_b:
            return False, 0
            
        return abs(l_d-r_d) <= 1, max(l_d, r_d)+1

