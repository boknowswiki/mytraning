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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        self.ret = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if low <= node.val <= high:
                self.ret += node.val
            dfs(node.right)

            return
        dfs(root)

        return self.ret
