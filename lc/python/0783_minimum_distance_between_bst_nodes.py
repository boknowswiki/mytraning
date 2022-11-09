
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ret = sys.maxsize
        self.prev = None
        self.helper(root)
        return self.ret
    
    def helper(self, node):
        if not node:
            return
        
        self.helper(node.left)
        if self.prev is None:
            self.prev = node.val
        else:
            self.ret = min(self.ret, node.val-self.prev)
            self.prev = node.val
            
        self.helper(node.right)
        
        return
    
# binary tree and inorder and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        arr = []
        self.inorder(root, arr)
        
        ret = sys.maxsize
        for i in range(1, len(arr)):
            ret = min(ret, arr[i]-arr[i-1])
            
        return ret
    
    def inorder(self, node, arr):
        if not node:
            return
        
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
        return
