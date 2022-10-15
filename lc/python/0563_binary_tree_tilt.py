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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        if not root:
            return self.ret
        
        self.helper(root)
        return self.ret
    
    def helper(self, node):
        if not node:
            return 0
        
        if node.left == None and node.right == None:
            return node.val
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        self.ret += abs(left-right)
        
        return left+right+node.val
