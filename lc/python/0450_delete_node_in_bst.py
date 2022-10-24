# binary tree and dfs
# time O(h)
# space O(1)

# reference https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # root.val == key
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
                
            tmp.val, root.val = root.val, tmp.val
            root.right = self.deleteNode(root.right, key)
            
        return root
