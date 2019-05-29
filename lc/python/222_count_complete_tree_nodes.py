#!/usr/bin/python -t

#time O(lgn^2) 

#If left sub tree height equals right sub tree height then,
#a. left sub tree is perfect binary tree
#b. right sub tree is complete binary tree
#If left sub tree height greater than right sub tree height then,
#a. left sub tree is complete binary tree
#b. right sub tree is perfect binary tree
#Note that mentioning full binary tree can create confusion because of the definition https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
#
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
        def get_depth(root):
            if root == None:
                return 0
            return 1 + get_depth(root.left)
        
        if root == None:
            return 0
        
        left_cnt = get_depth(root.left)
        right_cnt = get_depth(root.right)
        
        if left_cnt == right_cnt:
            return pow(2, left_cnt) + self.countNodes(root.right)
        else:
            return pow(2, right_cnt) + self.countNodes(root.left)

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
        ret = 0
        
        while root:
            l, r = map(self.getdepth, (root.left, root.right))
            if l == r:
                ret += 2**l
                root = root.right
            else:
                ret += 2**r
                root = root.left
                
        return ret
    
    def getdepth(self, node):
        dep = 0
        while node:
            dep += 1
            node = node.left
            
        return dep
