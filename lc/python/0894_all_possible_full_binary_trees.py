# dp, dfs with memo
# time O(2^(n/2))
# space O(n*2^(n/2))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]

        ret = []

        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-1-i)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    ret.append(root)

        return ret
