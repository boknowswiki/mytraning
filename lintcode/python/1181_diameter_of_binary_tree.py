#!/usr/bin/python -t

# tree traversal solution
#最长路径有两种情况：
#1.最长条路径经过根节点，那么只需要找出根节点的左右两棵子树的最大深度然后相加即可。
#2.最长路径没有经过根节点，那么只需要找出根节点的左子树或者根节点的右子树作为根的最长路径度即可。递归调用，
#自底向上查找子树的深度，如果某一个左子树与右子树深度之和大于当前纪录的直径，那么替换为当前直径，递归完成之后即可找出直径。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def __init__(self):
        self.max = 0
        
    def diameterOfBinaryTree(self, root):
        # write your code here
        ret = 0
        
        if root == None:
            return ret
        
        self.helper(root)
        
        return self.max
        
    def helper(self, node,):
        if node == None:
            return 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        self.max = max(self.max, left+right)
        
        return 1+max(left,right)

