# binary tree and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2

        l1 = []
        l2 = []
        def dfs(node, l):
            if not node:
                return
            if not node.left and not node.right:
                l.append(node.val)
                return
            dfs(node.left, l)
            dfs(node.right, l)

            return

        dfs(root1, l1)
        dfs(root2, l2)

        return l1 == l2
