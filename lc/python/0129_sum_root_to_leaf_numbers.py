

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if not root:
            return ret

        def dfs(node, val):
            nonlocal ret
            cur_val = 10*val + node.val
            if not node.left and not node.right:
                ret += cur_val
                return

            if node.left:
                dfs(node.left, cur_val)
            if node.right:
                dfs(node.right, cur_val)

            return

        dfs(root, 0)

        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ret = 0
        self.dfs(root, 0)
        return self.ret
    
    def dfs(self, node, val):
        if not node.left and not node.right:
            val = val * 10 + node.val
            self.ret += val
            return
        
        val = val*10 + node.val
        if node.left:
            self.dfs(node.left, val)
        if node.right:
            self.dfs(node.right, val)
            
        return
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ret = 0
        
        self.helper(root, 0)
        
        return self.ret
    
    def helper(self, node, val):
        if not node:
            return
        if node.left == None and node.right == None:
            val += node.val
            self.ret += val
            return
        
        val += node.val
        self.helper(node.left, val*10)
        self.helper(node.right, val*10)
        
        return
      
# someone's bfs

    def sumNumbers2(self, root): # BFS with queue
        deque, res = collections.deque(), 0
        if root:
            deque.append(root)
        while deque:
            node = deque.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val*10
                deque.append(node.left)
            if node.right:
                node.right.val += node.val*10
                deque.append(node.right)
        return res
