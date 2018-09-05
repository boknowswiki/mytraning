#!/usr/bin/python -t

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

