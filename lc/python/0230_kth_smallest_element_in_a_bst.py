# binary tree and dfs
# time O(logn)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.val = 0
        
        self.helper(root, k)
        
        return self.val
    
    def helper(self, node, k):
        if not node:
            return
        
        self.helper(node.left, k)
        self.index += 1
        if self.index == k:
            self.val = node.val
        self.helper(node.right, k)
        
        return
      
# bfs

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
