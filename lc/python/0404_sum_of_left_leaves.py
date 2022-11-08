
# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if not root:
            return ret
        
        q = collections.deque([root])
        
        while q:
            cur = q.popleft()
            if cur.left and cur.left.left is None and cur.left.right is None:
                ret += cur.left.val
                
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
        return ret

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        self.helper(root, False)
        return self.ret
    
    def helper(self, node, is_left):
        if not node:
            return
        if node.left == None and node.right == None and is_left:
            self.ret += node.val
            
        self.helper(node.left, True)
        self.helper(node.right, False)
        
        return
