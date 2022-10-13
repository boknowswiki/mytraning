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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        
        self.helper(root)
        
        return self.ret
    
    def helper(self, node):
        if not node:
            return 0
        if node.left == None and node.right == None:
            return 1
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        #print(f"node val {node.val}, left {left}, right {right}")
        
        self.ret = max(self.ret, left+right)
        return max(left+1, right+1)
