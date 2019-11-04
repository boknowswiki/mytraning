#!/usr/bin/python -t

# linked list

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return head
            
        self.copyNext(head)
        self.copyRandom(head)
        
        return self.split(head)
        
    def copyNext(self, head):
        while head:
            copy_head = RandomListNode(head.label)
            copy_head.random = head.random
            copy_head.next = head.next
            head.next = copy_head
            head = head.next.next
        
        return
    
    def copyRandom(self, head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
                
            head = head.next.next
            
        return
    
    def split(self, head):
        new_head = head.next
        
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            
            if tmp.next:
                tmp.next = tmp.next.next
                
        return new_head
        
        
