# tree, binary tree, bfs
# time O(n)
# space O(n)

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = collections.deque([root])
        should_stop = False

        while q:
            level = collections.deque([])
            has_empty = False
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is None and node.right is not None:
                    return False

                if node.left:
                    if not has_empty:
                        level.append(node.left)
                    else:
                        return False
                else:
                    has_emtpy = True
                
                if node.right:
                    if not has_empty:
                        level.append(node.right)
                    else:
                        return False
                else:
                    has_empty = True

            if should_stop and len(level) != 0:
                return False
            if has_empty:
                should_stop = True

            q = level

        return True
      
class Solution {
    public boolean isCompleteTree(TreeNode root) {
        if (root == null) {
            return true;
        }

        boolean nullNodeFound = false;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            TreeNode node = q.poll();

            if (node == null) {
                nullNodeFound = true;
            } else {
                if (nullNodeFound) {
                    return false;
                }
                q.offer(node.left);
                q.offer(node.right);
            }
        }
        return true;
    }
}
