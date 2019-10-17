#!/usr/bin/python -t

# dfs, inorder array and then find the minimum difference

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        # Write your code here
        self.nums = []
        
        self.inorder(root)
        
        ret = sys.maxint
        
        for i in range(1, len(self.nums)):
            ret = min(ret, self.nums[i]-self.nums[i-1])
            
        return ret
        
        
    def inorder(self, node):
        if node == None:
            return
        
        self.inorder(node.left)
        self.nums.append(node.val)
        self.inorder(node.right)
        
        return

