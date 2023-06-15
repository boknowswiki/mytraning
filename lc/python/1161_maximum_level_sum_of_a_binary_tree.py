# binary tree, bfs
# time O(n)
# space O(n)

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque([root])
        max_val = -sys.maxsize-1
        ret = 0
        level = 0

        while q:
            total = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                total += node.val

            if total > max_val:
                max_val = total
                ret = level

        return ret
      
      
# dfs

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, level: int, sum_at_current_level: List) -> None:
            if not node:
                return

            if len(sum_at_current_level) == level:
                sum_at_current_level.append(node.val)
            else:
                sum_at_current_level[level] += node.val

            dfs(node.left, level + 1, sum_at_current_level)
            dfs(node.right, level + 1, sum_at_current_level)

        sum_at_current_level = []    
        dfs(root, 0, sum_at_current_level)

        return 1 + sum_at_current_level.index(max(sum_at_current_level))
