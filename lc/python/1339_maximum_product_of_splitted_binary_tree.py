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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        ret = root.val

        def get_sum(node):
            nonlocal total

            if not node:
                return
            get_sum(node.left)
            total += node.val
            get_sum(node.right)
            return

        get_sum(root)

        def dfs(node):
            nonlocal ret
            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            ret_val = node.val + left + right
            ret = max(ret, (ret_val)*(total-ret_val))

            return ret_val

        dfs(root)

        return ret%(10**9+7)
      
      
 def maxProduct(self, root: TreeNode) -> int:
    all_sums = []

    def tree_sum(subroot):
        if subroot is None: return 0
        left_sum = tree_sum(subroot.left)
        right_sum = tree_sum(subroot.right)
        total_sum = left_sum + right_sum + subroot.val
        all_sums.append(total_sum)
        return total_sum

    total = tree_sum(root)
    best = 0
    for s in all_sums:
        best = max(best, s * (total - s))   
    return best % (10 ** 9 + 7)
