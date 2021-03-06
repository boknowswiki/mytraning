#!/usr/bin/python -t

#对于原来的BST来说：
#
#若根节点的值小于最小值，则递归调用右子树并返回右子树；
#若根节点的值大于最大值，则递归调用左子树并返回左子树；
#否则修剪左子树，右子树并返回根节点。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trimBST(self, root, minimum, maximum):
        # write your code here
        if root == None:
            return None
            
        if root.val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        elif root.val > maximum:
            return self.trimBST(root.left, minimum, maximum)
        else:
            root.left = self.trimBST(root.left, minimum, maximum)
            root.right = self.trimBST(root.right, minimum, maximum)
            
        return root
        
