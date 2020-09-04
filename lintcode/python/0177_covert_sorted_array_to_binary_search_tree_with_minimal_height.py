#!/usr/bin/pythoh -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return None
            
        root = self.helper(A, 0, len(A)-1)
        
        return root
        
    def helper(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        
        mid = (start+end)/2
        root = TreeNode(A[mid])
        root.left = self.helper(A, start, mid-1)
        root.right = self.helper(A, mid+1, end)
        
        return root
