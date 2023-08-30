#!/usr/bin/python -t

# binary tree

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            cur, val = stack.pop()
            if cur.left == None and cur.right == None:
                if val == sum:
                    return True
                
            if cur.right:
                stack.append((cur.right, val+cur.right.val))
            if cur.left:
                stack.append((cur.left, val+cur.left.val))

                
        return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
