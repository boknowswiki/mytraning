
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
        if not root:
            return 0

        ret = sys.maxsize
        prev = None

        def helper(node):
            nonlocal ret, prev

            if not node:
                return

            helper(node.left)
            if prev == None:
                prev = node
            else:
                ret = min(ret, abs(prev.val-node.val))
                prev = node

            helper(node.right)

            return

        helper(root)

        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.prev = None
        self.ret = sys.maxsize
        self.helper(root)
        
        return self.ret
    
    def helper(self, node):
        if not node:
            return
        
        self.helper(node.left)
        if self.prev is None:
            self.prev = node
        else:
            self.ret = min(self.ret, abs(self.prev.val - node.val))
            self.prev = node
        self.helper(node.right)
        
        return

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
