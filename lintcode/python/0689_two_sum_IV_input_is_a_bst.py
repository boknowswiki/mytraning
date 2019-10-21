#!/usr/bin/python -t

# inorder and bsf

#用inorder遍历。
#遍历过程中根据BST的性质用类似二分的方法查找。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
            
        self.ret = None
        node_set = set()
        
        self.inorder(root, n, node_set)
        
        return self.ret
        
    def inorder(self, root, n, node_set):
        if root == None:
            return
        self.inorder(root.left, n, node_set)
        
        if root.val in node_set:
            self.ret = [root.val, n-root.val]
        else:
            node_set.add(n-root.val)
        self.inorder(root.right, n, node_set)
        
        return
    
