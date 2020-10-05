"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        # write your code here
        if root == None:
            return []
            
        ret = []
        q = [root]
        
        while len(q) != 0:
            max_val = -sys.maxint-1
            n = len(q)
            
            for i in range(n):
                node = q.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ret.append(max_val)
            
        return ret
