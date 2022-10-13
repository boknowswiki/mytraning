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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ret = sys.maxsize
        inorder = []
        self.helper(root, inorder)
        
        for i in range(1, len(inorder)):
            ret = min(ret, inorder[i]-inorder[i-1])
            
        return ret
    
    def helper(self, node, inorder):
        if not node:
            return 0
        
        self.helper(node.left, inorder)
        inorder.append(node.val)
        self.helper(node.right, inorder)
        
        return
