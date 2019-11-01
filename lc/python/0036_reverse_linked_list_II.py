#!/usr/bin/python -t

# linked list

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or m > n:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(1, m):
            if prev == None:
                return None
                
            prev = prev.next
        
        m_node = prev.next
        n_node = m_node
        post_n = n_node.next
        for _ in range(m,n):
            if post_n == None:
                return None
                
            tmp = post_n.next
            post_n.next = n_node
            n_node = post_n
            post_n = tmp
            
        m_node.next = post_n
        prev.next = n_node
        
        return dummy.next
        
        
            
