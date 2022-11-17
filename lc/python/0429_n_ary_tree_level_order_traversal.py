# bfs
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []
        if not root:
            return ret
        
        q = collections.deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                for c in cur.children:
                    if c != None:
                        q.append(c)
                        
            ret.append(list(level))
            
        return ret
