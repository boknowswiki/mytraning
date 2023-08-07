# linked list
# time O(n)
# space O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        cur = head

        def dfs(node):
            prev = node
            while node:
                if node.child:
                    tmp = dfs(node.child)
                    tmp.next = node.next
                    if node.next:
                        node.next.prev = tmp
                    node.next = node.child
                    node.child.prev = node
                    node.child = None

                prev = node
                node = node.next

            return prev

        while cur:
            if cur.child:
                tmp = dfs(cur.child)
                tmp.next = cur.next
                if cur.next:
                    cur.next.prev = tmp
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            cur= cur.next

        return head


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next
