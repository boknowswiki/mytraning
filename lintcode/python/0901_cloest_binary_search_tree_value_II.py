#!/usr/bin/python -t

# binary search tree inorder traversal and binary search.
#time O(n) space O(n)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root or k == 0:
            return []

        ret = []
        nums = []
        self.get_inorder(root, nums)

        left = self.find_lower(nums, target)
        right = left +1

        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                ret.append(nums[left])
                left -= 1
            else:
                ret.append(nums[right])
                right += 1

        return ret

    def get_inorder(self, root, nums):
        if not root:
            return

        self.get_inorder(root.left, nums)
        nums.append(root.val)
        self.get_inorder(root.right, nums)

        return

    def find_lower(self, nums, target):
        left = 0
        right = len(nums)-1

        while left + 1 < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[right] < target:
            return right
        if nums[left] < target:
            return left

        return -1
        
    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True

        if abs(nums[left]-target) <= abs(nums[right]-target):
            return True
        return False
