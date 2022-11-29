# binary tree and dfds
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.first, self.second = None, None
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            if self.prev is not None and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            dfs(node.right)
            
            return
            
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        return

# binary tree and iterative
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val < prev.val: drops.append((prev, node))
            prev, cur = node, node.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

# binary tree and dfs

    def recoverTree1(self, root): # O(n+lg(n)) space  
        res = []
        self.dfs(root, res)
        first, second = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val and not first:
                first = res[i]
            if res[i].val > res[i+1].val and first:
                second = res[i+1]
        first.val, second.val = second.val, first.val
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root)
            self.dfs(root.right, res)
