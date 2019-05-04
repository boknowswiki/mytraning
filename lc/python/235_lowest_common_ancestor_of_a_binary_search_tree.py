#!/usr/bin/python -t

#time O(n) space O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        
        while node:
            p_val = node.val
            if p.val < p_val and q.val < p_val:
                node = node.left
            elif p.val > p_val and q.val > p_val:
                node = node.right
            else:
                return node


#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lowestcomm(node, p, q):
            if p.val < node.val and q.val < node.val:
                return lowestcomm(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return lowestcomm(node.right, p, q)
            else:
                return node
            
        return lowestcomm(root, p, q)
