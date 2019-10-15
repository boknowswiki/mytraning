#!/usr/bin/python -t

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
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        # write your code here
        self.mapping = {}
        
        sum = self.dfs(root)
        if sum == 0:
            return self.mapping[sum] > 1
            
        return sum%2 == 0 and not self.mapping.get(sum/2) == None
        
    def dfs(self, node):
        if node == None:
            return 0
        
        sum = self.dfs(node.left) + self.dfs(node.right) + node.val
        
        if sum not in self.mapping:
            self.mapping[sum] = 1
        else:
            self.mapping[sum] += 1
            
        return sum
        
