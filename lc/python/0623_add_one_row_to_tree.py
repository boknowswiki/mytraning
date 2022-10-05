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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val)
            new_root.left = root
            return new_root
        
        q = collections.deque([root])
        
        while q:
            depth -= 1
            for _ in range(len(q)):
                node = q.popleft()
                if depth == 1:
                    left = TreeNode(val=val)
                    right = TreeNode(val=val)
                    left.left = node.left
                    right.right = node.right
                    node.left = left
                    node.right = right
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
        return root
            
