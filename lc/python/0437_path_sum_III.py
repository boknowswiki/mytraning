# binary tree and dfs and presum and memorization
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, targetSum, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ret = 0

        self.helper(root, targetSum)
        
        return self.ret
    
    def helper(self, node, target):
        if not node:
            return
            
        self.helper1(node, target)
        self.helper(node.left, target)
        self.helper(node.right, target)

        return
    
    def helper1(self, node, target):
        if not node:
            return
                
        #print(f"node {node.val}, target {target}")
        if node.val == target:
            self.ret += 1
            
        self.helper1(node.left, target-node.val)
        self.helper1(node.right, target-node.val)
        
        return
