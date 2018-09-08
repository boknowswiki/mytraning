#!/usr/bin/python -t

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


