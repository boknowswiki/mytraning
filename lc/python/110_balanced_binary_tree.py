#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l_b, l_l = self.helper(root.left)
        r_b, r_l = self.helper(root.right)
        
        return l_b and r_b and (abs(l_l - r_l) <= 1)
    
    def helper(self, node):
        if not node:
            return True, 0
        
        l_b, l_l = self.helper(node.left)
        r_b, r_l = self.helper(node.right)
        
        if l_b and r_b and abs(l_l - r_l) <=1:
            return True, max(l_l, r_l) + 1
        return False, max(l_l, r_l) + 1
    
# iterative way

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
    

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


