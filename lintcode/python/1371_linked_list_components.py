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
    @param head: the head
    @param G: an array
    @return: the number of connected components in G
    """
    def numComponents(self, head, G):
        # Write your code here
        if not head:
            return 0
            
        g = set(G)
        ret = 0
        
        while head:
            if head.val in g and (not head.next or head.next.val not in g):
                ret += 1
                
            head = head.next
            
        return ret
        
        
# union find solution

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class uf:
    def __init__(self, s):
        self.f = {i:i for i in s}
        self.cnt = len(s)
        
    def find(self, x):
        if x not in self.f:
            return -1
            
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
    
        return self.f[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        
        if rx == -1 or ry == -1:
            return
        
        if rx == ry:
            return
        
        self.f[rx] = ry
        self.cnt -= 1
        
        return

class Solution:
    """
    @param head: the head
    @param G: an array
    @return: the number of connected components in G
    """
    def numComponents(self, head, G):
        # Write your code here
        s = set(G)
        myuf = uf(s)
        
        while head and head.next:
            myuf.union(head.val, head.next.val)
            head = head.next
            
        return myuf.cnt
