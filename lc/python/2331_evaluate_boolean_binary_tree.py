# binary tree and dfs
# time O(n)
# space o(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val != 2 and root.val != 3:
            return root.val
        
        return self.dfs(root)
    
    def dfs(self, node):
        if node.left is None and node.right is None:
            return node.val
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if node.val == 2:
            return left or right
        return left and right
