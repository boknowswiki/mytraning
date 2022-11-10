
# binary tree and bfs
# time O(n)
# space O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
               
        return root

# binary tree and bfs
# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = collections.deque([root])
        ret = None
        
        while q:
            l = len(q)
            prev = None
            for i in range(l):
                #print(f"l {l}, prev {prev}")
                node = q.popleft()
                #print(f"node {node.val}")
                if ret == None:
                    ret = node
                    node.next = None
                if prev == None:
                    prev = node
                else:
                    prev.next = node
                    prev = prev.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if prev != None:
                prev.next = None
            
        return ret
