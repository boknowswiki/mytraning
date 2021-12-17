#!/usr/bin/python -t


# binary search tree
# similar to 0915

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        suc = None
        while root:
            if root.val > p.val:
                suc = root
                root = root.left
            else:
                root = root.right

        return suc

#首先要确定中序遍历的后继:
#
#如果该节点有右子节点, 那么后继是其右子节点的子树中最左端的节点
#如果该节点没有右子节点, 那么后继是离它最近的祖先, 该节点在这个祖先的左子树内.
#使用循环实现:
#
#查找该节点, 并在该过程中维护上述性质的祖先节点
#查找到后, 如果该节点有右子节点, 则后继在其右子树内; 否则后继就是维护的那个祖先节点
#使用递归实现:
#
#如果根节点小于或等于要查找的节点, 直接进入右子树递归
#如果根节点大于要查找的节点, 则暂存左子树递归查找的结果, 如果是 null, 则直接返回当前根节点; 反之返回左子树递归查找的结果.
#在递归实现中, 暂存左子树递归查找的结果就相当于循环实现中维护的祖先节点.

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        s = None
        
        while root != None and root.val != p.val:
            if root.val > p.val:
                s = root
                root = root.left
            else:
                root = root.right
                
        if root == None:
            return None
            
        if root.right == None:
            return s
            
        root = root.right
        while root.left != None:
            root = root.left
            
        return root
       

# dfs, divid and conquer

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if root == None or p == None:
            return None
            
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left is not None else root
            

