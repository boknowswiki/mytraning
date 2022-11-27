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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ret = sys.maxsize
        self.min = root.val
        
        def dfs(node):
            if not node:
                return
            if self.min < node.val < self.ret:
                self.ret = node.val
            elif node.val == self.min:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        
        return self.ret if self.ret != sys.maxsize else -1
