#!/usr/bin/python -t

# dfs

# Time complexity: O(N)
# Space complexity: O(N)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, target):
        # Write your code here.
        result = []

        self.dfs(root, target, [], result)

        return result

    def dfs(self, node, target, permutation, result):
        if not node:
            return

        if target < 0:
            return

        if not node.left and not node.right and target == node.val:
            result.append(list(permutation + [node.val]))
            return

        permutation.append(node.val)
        self.dfs(node.left, target - node.val, permutation, result)
        self.dfs(node.right, target - node.val, permutation, result)
        permutation.pop()
