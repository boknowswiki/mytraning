#!/usr/bin/python -t

# binary tree
# divid and conquer way
# time O(n)
# space O(n)


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive(self, root: TreeNode) -> int:
        # write your code here
        if not root:
            return 0

        ret, _ = self.helper(root)

        return ret

    def helper(self, node):
        if not node:
            return 0, 0

        left, left_ret = self.helper(node.left)
        right, right_ret = self.helper(node.right)

        cur_ret = 1
        if node.left and node.val == node.left.val - 1:
            cur_ret = max(left_ret+1, cur_ret)

        if node.right and node.val == node.right.val - 1:
            cur_ret = max(right_ret+1, cur_ret)

        ret = max(cur_ret, left, right)

        return ret, cur_ret



# binary tree
# traversal and divid and conquer way
# time O(n)
# space O(n)

class Solution:
    def __init__(self):
        self.ret = 0

    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive(self, root: TreeNode) -> int:
        # write your code here
        if not root:
            return 0

        self.helper(root)

        return self.ret

    def helper(self, node):
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        ret = 1
        if node.left and node.val == node.left.val - 1:
            ret = max(left+1, ret)

        if node.right and node.val == node.right.val - 1:
            ret = max(right+1, ret)

        self.ret = max(self.ret, ret)

        return ret

# dfs, traversal and divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root, None, 0)
        
    def helper(self, node, parent, length):
        if node == None:
            return length
            
        if parent and node.val == parent.val+1:
            length += 1
        else:
            length = 1
            
        return max(length, self.helper(node.left, node, length),
                            self.helper(node.right, node, length))

