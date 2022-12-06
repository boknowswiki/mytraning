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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        def dfs(node):
            if not node:
                return
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                else:
                    dfs(node.left)
            elif val > node.val:
                if node.right is None:
                    node.right = TreeNode(val=val)
                else:
                    dfs(node.right)

            return

        dfs(root)
        return root
      
 class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)
