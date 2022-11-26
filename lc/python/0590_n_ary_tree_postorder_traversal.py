# tree and dfs
# time O(n)
# space O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        self.ret = []
        
        self.helper(root)
        
        return self.ret
    
    def helper(self, node):
        if not node:
            return None
        
        for c in node.children:
            self.helper(c)
            
        self.ret.append(node.val)
        
        return
