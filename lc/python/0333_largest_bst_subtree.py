# binary tree and dfs
# time O(n)
# space O(1)

# Each node will return min node value, max node value, size
class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largest_bst_subtree_helper(self, root):
        # An empty tree is a BST of size 0.
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)

        # Get values from left and right subtree of current tree.
        left = self.largest_bst_subtree_helper(root.left)
        right = self.largest_bst_subtree_helper(root.right)
        
        # Current node is greater than max in left AND smaller than min in right, it is a BST.
        if left.max_node < root.val < right.min_node:
            # It is a BST.
            return NodeValue(min(root.val, left.min_node), max(root.val, right.max_node), 
                             left.max_size + right.max_size + 1)
        
        # Otherwise, return [-inf, inf] so that parent can't be valid BST
        return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.largest_bst_subtree_helper(root).max_size
