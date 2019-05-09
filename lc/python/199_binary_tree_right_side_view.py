#!/usr/bin/python -t

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, level, ret):
            if root == None:
                return
            if level == len(ret):
                ret.append(root.val)
            dfs(root.right, level+1, ret)
            dfs(root.left, level+1, ret)
            
        ret = []
        dfs(root, 0, ret)
        return ret


#DFS

#time O(n) space O(n)

class Solution(object):
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # depth -> node.val
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)

                # only insert into dict if depth is not already present.
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


#BFS
#time O(n) space O(n)

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # depth -> node.val
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)

                # overwrite rightmost value at current depth. the correct value
                # will never be overwritten, as it is always visited last.
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
