#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS top to bottom
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def max_depth(root):
            if root == None:
                return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1

        if root == None:
            return True

        return abs(max_depth(root.left) - max_depth(root.right)) <= 1 and \
                self.isBalanced(root.left) and self.isBalanced(root.right)


#DFS bottom to top
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(root):
            if root == None:
                return 0

            left = balanced(root.left)
            if left == -1:
                return -1

            right = balanced(root.right)
            if right == -1:
                return -1

            return max(left, right)+1 if abs(left-right) <= 1 else -1

        if root == None:
            return True
        return balanced(root) != -1


