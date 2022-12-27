# linked list, binary tree
# time O(n)
# space O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        head = None
        tail = None

        def dfs(node):
            nonlocal head, tail
            if not node:
                return None

            dfs(node.left)
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node

            tail = node

            dfs(node.right)

        dfs(root)

        head.left = tail
        tail.right = head

        return head
