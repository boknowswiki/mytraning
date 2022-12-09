# binary tree and dfs
# time O(n)
# space O(1)

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)

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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ret = 0

        def dfs(node, path):
            #print(f"path {path}")
            nonlocal ret
            if not node.left and not node.right:
                path.append(node.val)
                ret = max(ret, abs(max(path)-min(path)))
                path.pop()
                return

            path.append(node.val)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

            return

        dfs(root, [])

        return ret
