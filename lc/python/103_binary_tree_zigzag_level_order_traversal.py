#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root == None:
            return ret
        
        s = [root]
        left_to_right = 1
        
        while s:
            level = []
            for i in range(len(s)):
                node = s.pop(0)
                level.append(node.val)
                
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
                 
            ret.append(level[::left_to_right])
            left_to_right = -1 * left_to_right
             
        return ret
