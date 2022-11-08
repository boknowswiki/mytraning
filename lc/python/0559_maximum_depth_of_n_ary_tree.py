# tree and bfs
# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        ret = 0
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for c in cur.children:
                    q.append(c)
                    
            ret += 1
            
        return ret
