# bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        bfs = [root]
        exists = set()
        
        while bfs:
            for _ in range(len(bfs)):
                node = bfs.pop()
                if k-node.val in exists:
                    return True
                exists.add(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                    
        return False
      
# bst iteration and two pointers
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        self.convert_to_array(root, arr)
        l = 0
        r = len(arr)-1
        while l < r:
            val = arr[l] + arr[r]
            if val == k:
                return True
            elif val < k:
                l += 1
            else:
                r -= 1
                
        return False
    
    def convert_to_array(self, node, arr):
        if not node:
            return
        
        self.convert_to_array(node.left, arr)
        arr.append(node.val)
        self.convert_to_array(node.right, arr)
        
        return
