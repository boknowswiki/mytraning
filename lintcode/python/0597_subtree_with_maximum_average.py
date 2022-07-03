#!/usr/bin/python -t

# binary tree
# divid and conquer way
# time O(n)
# space O(1)

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        if not root:
            return root

        node, max_avg, total, cnt = self.helper(root)

        return node

    def helper(self, node):
        if not node:
            return None, 0, 0, 0

        left_node, l_max_avg, l_total, l_cnt = self.helper(node.left)
        right_node, r_max_avg, r_total, r_cnt = self.helper(node.right)

        total = node.val + l_total + r_total
        cnt = 1 + l_cnt + r_cnt
        max_avg = total / cnt

        if left_node is not None and l_max_avg >= r_max_avg and l_max_avg > max_avg:
            return left_node, l_max_avg, total, cnt
        if right_node is not None and r_max_avg >= l_max_avg and r_max_avg > max_avg:
            return right_node, r_max_avg, total, cnt

        return node, max_avg, total, cnt

# dfs, divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    
    def __init__(self):
        self.avg = 0
        self.node = None
        
    def findSubtree2(self, root):
        # write your code here
        if root == None:
            return self.node
            
        self.helper(root)
        
        return self.node
        
    def helper(self, node):
        if node == None:
            return 0, 0
            
        l_size, l_sum = self.helper(node.left)
        
        r_size, r_sum = self.helper(node.right)
        
        n_sum = (l_sum + r_sum + node.val)
        
        n_avg = (n_sum*1.0)/(l_size+r_size+1)
        
        if self.node == None or n_avg > self.avg:
            self.avg = n_avg
            self.node = node
            
        return (l_size+r_size+1), n_sum

