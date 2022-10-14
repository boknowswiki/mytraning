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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        self.helper(root, False)
        return self.ret
    
    def helper(self, node, is_left):
        if not node:
            return
        if node.left == None and node.right == None and is_left:
            self.ret += node.val
            
        self.helper(node.left, True)
        self.helper(node.right, False)
        
        return
