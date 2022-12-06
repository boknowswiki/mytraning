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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if not root:
            return ret

        def dfs(node, parent, length):
            nonlocal ret
            if not node:
                return
            length = length + 1 if parent != None and parent.val + 1 == node.val else 1
            ret = max(ret, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)
            return

        dfs(root, None, 0)
        return ret
