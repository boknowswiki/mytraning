#!/usr/bin/python -t

# dp

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: return the min steps
    """
    def makeBinaryTreeAverage(self, root):
        # write your code here
        dp = dict()
        _, max_distance, min_distance = self.helper(root, dp)
        return min_distance
        
    def helper(self, node, dp):
        if not node:
            return ({}, 0, 0)
            
        left_dict, left_max_distance, left_min_distance = self.helper(node.left, dp)
        right_dict, right_max_distance, right_min_distance = self.helper(node.right, dp)
        node_dict = {}
        
        if not node.left and not node.right:
            dp[node] = ({node.val: 0}, 1, 0)
            return dp[node]
        
        if not node.left:
            for key in right_dict:
                node_dict[key] = right_dict[key] + 1
            if node.val in right_dict:
                node_dict[node.val] = right_dict[node.val]
            else:
                node_dict[node.val] = right_max_distance
            min_distance = min(node_dict.values())
            max_distance = right_max_distance + 1
            dp[node] = (node_dict, max_distance, min_distance)
            return dp[node]
            
        if not node.right:
            for key in left_dict:
                node_dict[key] = left_dict[key] + 1
            if node.val in left_dict:
                node_dict[node.val] = left_dict[node.val]
            else:
                node_dict[node.val] = left_max_distance
            min_distance = min(node_dict.values())
            max_distance = left_max_distance + 1
            dp[node] = (node_dict, max_distance, min_distance)
            return dp[node]
            
        if node.left and node.right:
            max_distance = min(left_max_distance + right_min_distance + 1, left_min_distance + right_max_distance + 1)
            for left_key in left_dict:
                for right_key in right_dict:
                    if (left_key + right_key) / 2 == node.val:
                        node_dict[(left_key + right_key) / 2] = left_dict[left_key] + right_dict[right_key]
                    else:
                        node_dict[(left_key + right_key) / 2] = left_dict[left_key] + right_dict[right_key] + 1
            if node.val not in node_dict:
                node_dict[node.val] = min(left_max_distance + right_min_distance, left_min_distance + right_max_distance)
            min_distance = min(node_dict.values())
            dp[node] = (node_dict, max_distance, min_distance)
            return dp[node]
