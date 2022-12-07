# binary tree and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_table = collections.defaultdict(list)
        min_col = max_col = 0

        def dfs(node, row, col):
            nonlocal min_col
            nonlocal max_col
            if not node:
                return
            col_table[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)

            return
            
        dfs(root, 0, 0)

        ret = []
        for i in range(min_col, max_col+1):
            col_table[i].sort(key=lambda x:x[0])
            ret.append([v for _, v in col_table[i]])

        return ret
