#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, start, end):
        if start > end:
            return None
        
        if start == end:
            return TreeNode(val=nums[start])
        
        mid = start + (end-start)//2
        node = TreeNode(val=nums[mid])
        node.left = self.helper(nums, start, mid-1)
        node.right = self.helper(nums, mid+1, end)
        
        return node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _iterative(self, a):
        root, stack = None, [(0, len(a)-1, None, None)]
        while stack:
            lo, hi, l_parent, r_parent = stack.pop()
            if lo > hi:
                continue
            mid = lo + (hi-lo)//2
            node = TreeNode(a[mid])
            root = root or node
            if l_parent:
                l_parent.left = node
            if r_parent:
                r_parent.right = node
            stack.append((lo, mid-1, node, None))
            stack.append((mid+1, hi, None, node))
        return root

    def sortedArrayToBST(self, a):
        '''Convert a sorted array to a BST in O(n) time and O(log n) space.'''
        return self._iterative(a)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def sortedarraytobst(nums, start, end):
            if start > end:
                return None
            mid = (start + end)/2
            root = TreeNode(nums[mid])
            root.left = sortedarraytobst(nums, start, mid-1)
            root.right = sortedarraytobst(nums, mid+1, end)

            return root

        return sortedarraytobst(nums, 0, len(nums) - 1)


