# dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ret = 0
        self.dfs(root)
        return self.ret
    
    def dfs(self, node):
        if not node.left and not node.right:
            self.ret += 1
            return True
        
        is_uni = True
        if node.left:
            is_uni = self.dfs(node.left) and is_uni and node.left.val == node.val
        if node.right:
            is_uni = self.dfs(node.right) and is_uni and node.right.val == node.val
            
        self.ret += is_uni
        
        return is_uni
