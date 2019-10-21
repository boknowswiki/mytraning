#!/usr/bin/python -t

# other solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         一直向左下走来计算深度
        def getDepth(Node):
            if Node == None:
                return 0
            
            depth = 1
            while Node.left != None:
                depth += 1
                Node = Node.left
            
            return depth
        
        if root == None:
            return 0
        
        rightT = root.right
        leftT = root.left
        rDepth = getDepth(rightT)
        lDepth = getDepth(leftT)
#         如果左右子树深度相同，那么说明右子数是满二叉树，左子树是完全二叉树
        if rDepth == lDepth:
            return self.countNodes(rightT) + 2 ** lDepth 
#         否则说明左子树是满二叉树，右子树是完全二叉树
        else:
            return self.countNodes(leftT) + 2 ** rDepth


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
    @param root: root of complete binary tree
    @return: the number of nodes
    """
    def countNodes(self, root):
        # write your code here
        if root == None:
            return 0
            
        if root.left == None and root.right == None:
            return 1
            
        left_cnt = self.countNodes(root.left)
        right_cnt = self.countNodes(root.right)
        
        return 1 + left_cnt + right_cnt
        
        
