#!/usr/bin/python -t

# linked list, not AC, union find set

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given doubly linked list
    @param nodes: the given nodes array
    @return: the number of blocks in the given array
    """
    
    def __init__(self):
        self.father = [i for i in range(1000)]
        
    def find(self, p):
        if self.father[p] == p:
            return p
            
        self.father[p] = self.find(self.father[p])
        
        return self.father[p]
        
    def union(self, p, q):
        father_p = self.find(p)
        father_q = self.find(q)
        
        if father_q = father_p:
            return
        
        self.father[p] = father_q
        
        return
    
    def blockNumber(self, head, nodes):
        # write your code here
        if not head:
            return 0
         
        ret = 0   
        v = set()
        
        for i in range(nodes):
            v.add(i)
            
        cur = head
        
        while cur.next:
            if cur.val in v and cur.next.val in v:
                self.union(cur.val, cur.next.val)
                
            cur = cur.next
            
        for i in nodes:
            self.find(i) == i:
                ret += 1
                
        return ret
        
        

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given doubly linked list
    @param nodes: the given nodes array
    @return: the number of blocks in the given array
    """
    def blockNumber(self, head, nodes):
        # write your code here
        if not head:
             return 0
             
        v = set()
        ret = 0
        
        for i in nodes:
            v.add(i)
            
        while head:
            if head.val in v and (head.next == None or head.next.val not in v):
                ret += 1
                
            head = head.next
            
        return ret
        
        
