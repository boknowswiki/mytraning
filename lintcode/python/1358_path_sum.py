#!/usr/bin/python -t

# dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the tree
    @param sum: the sum
    @return:  if the tree has a root-to-leaf path
    """
    def pathSum(self, root, sum):
        # Write your code here.
        if sum < 0:
            return False
        if not root and sum == 0:
            return True
        if not root and sum != 0:
            return False

        if root.left == None and root.right == None and sum == root.val:
            return True

        return self.pathSum(root.left, sum-root.val) or self.pathSum(root.right, sum-root.val)




class Solution:
    """
    @param root: the tree
    @param sum: the sum
    @return:  if the tree has a root-to-leaf path
    """
    def pathSum(self, root, sum):
        # Write your code here.
        if root == None:
            return False;
        elif (root.val == sum and root.left == None and root.right == None):
            return True;
        else:
            return self.pathSum(root.left, sum - root.val) or self.pathSum(root.right, sum - root.val);
