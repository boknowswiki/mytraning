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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.ret = []
        
        self.dfs(root, targetSum, [])
        
        return self.ret
    
    def dfs(self, node, target, path):
        if node.left == None and node.right == None:
            if node.val == target:
                path.append(node.val)
                self.ret.append(list(path))
            return
        if node.left:
            self.dfs(node.left, target-node.val, path+[node.val])
            
        if node.right:
            self.dfs(node.right, target-node.val, path+[node.val])
            
        return

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ret = []
        
        self.helper(root, targetSum, [], ret)
        
        return ret
    
    def helper(self, node, target, path, ret):
        if node.left == None and node.right == None:
            if node.val == target:
                path.append(node.val)
                ret.append(list(path))
                path.pop()
            return
        
        path.append(node.val)
        if node.left:
            self.helper(node.left, target-node.val, path, ret)
        
        if node.right:
            self.helper(node.right, target-node.val, path, ret)
        path.pop()
        return
      
 # someone's bfs
    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
