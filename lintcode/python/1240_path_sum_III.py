#!/usr/bin/python -t

# bfs

from collections import deque

class Solution:
    def pathSum(self, root, sum):
        # write your code here
        queue = deque([(root, root.val)])

        count = 0
        checked = set()
        while queue:
            cur, cur_sum = queue.popleft()
            if (cur, cur_sum) in checked:
                continue
            checked.add((cur, cur_sum))
            if cur_sum == sum:
                count += 1
            if cur.left:
                queue.append((cur.left, cur.left.val))
                queue.append((cur.left, cur.left.val + cur_sum))
            if cur.right:
                queue.append((cur.right, cur.right.val))
                queue.append((cur.right, cur.right.val + cur_sum))

        return count

# dfs

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root:
    @param sum:
    @return: the num of sum path
    """
    def pathSum(self, root, sum):
        # write your code here
        if not root:
            return 0

        self.count = 0
        self.dfs(root, sum, [root.val])

        return self.count

    def dfs(self, node, target, path):

        s = 0
        for i in range(len(path)-1, -1, -1):
            s += path[i]
            if s == target:
                self.count += 1

        if node.left:
            self.dfs(node.left, target, path+[node.left.val])
        if node.right:
            self.dfs(node.right, target, path+[node.right.val])
