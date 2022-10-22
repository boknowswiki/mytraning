# binary tree and dp
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))
    
    def helper(self, node):
        if not node:
            return 0, 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        now = node.val + left[1] + right[1]
        
        later = max(left) + max(right)
        
        return now, later
