# dfs, binary tree
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0

        ret = 0
        def dfs(node, go_left, steps):
            nonlocal ret
            if node:
                ret = max(ret, steps)
                if go_left:
                    dfs(node.left, False, steps+1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.right, True, steps+1)
                    dfs(node.left, False, 1)
            

        dfs(root, False, 0)
        dfs(root, True, 0)

        return ret
