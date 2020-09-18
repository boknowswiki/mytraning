#!/usr/bin/python -t

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param root: the tree
    @return: pre order of the tree
    """
    def preorder(self, root):
        # write your code here
        if not root:
            return root
            
        stack = [root]
        ret = []
        
        while len(stack) != 0:
            node = stack.pop()
            ret.append(node.label)
            stack.extend(node.neighbors[::-1])
            
        return ret
