#!/usr/bin/python -t

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
    @param nums: the sorted array
    @return: the root of the tree
    """
    def convertSortedArraytoBinarySearchTree(self, nums):
        # Write your code here.
        ret = self.helper(nums, 0, len(nums)-1)
        
        return ret
        
    def helper(self, nums, start, end):
        if start > end:
            return None
            
        mid = (start+end)/2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, start, mid-1)
        node.right = self.helper(nums, mid+1, end)
        
        return node
        
