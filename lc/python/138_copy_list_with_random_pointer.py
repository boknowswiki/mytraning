#!/usr/bin/python -t

# linked list

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        v = set()
        cur = head
        # copy nodes
        while cur:
            tmp = cur.next
            clone = Node(cur.val)
            cur.next = clone
            clone.next = tmp
            cur = tmp
        
        # copy randome nodes
        cur = head
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # split clone nodes
        dummy = Node(x=0)
        prev = dummy
        cur = head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev = prev.next
            cur = cur.next

        return dummy.next

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return head

        cur = head

        while cur:
            next = cur.next
            copy = RandomListNode(cur.label)
            cur.next = copy
            copy.next = next
            cur = next

        cur = head

        while cur:
            if cur.random != None:
                cur.next.random = cur.random.next

            cur = cur.next.next

        cur = head
        dummy = RandomListNode(cur.label)
        copyhead = dummy

        while cur:
            copyhead.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            copyhead = copyhead.next

        return dummy.next

