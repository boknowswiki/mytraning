# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        self.ret = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.val > p.val:
                if self.ret == None:
                    self.ret = node
                elif node.val < self.ret.val:
                    self.ret =  node

            dfs(node.right)

        dfs(root)

        return self.ret
        
# binary tree

class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor
