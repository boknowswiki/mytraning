#!/usr/bin/python -t

# linked list with divid and conquer

# time O(nlogk)

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        n = len(lists)
        if n == 0:
            return None
            
        return self.helper(lists, 0, n-1)
            
            
    def helper(self, lists, start, end):
        if start == end:
            return lists[start]
            
        mid = (end-start)/2+start
        
        left = self.helper(lists, start, mid)
        right = self.helper(lists, mid+1, end)
        
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
            
        dummy = ListNode(0)
        prev = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
                
            prev = prev.next
            
        if l1:
            prev.next = l1
        else:
            prev.next = l2
            
        return dummy.next
        

# heap solution
        
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        from heapq import heappush, heappop
        heap = []
        for node in lists:
            if node:
                heappush(heap, (node.val, node))
        dummy = ListNode(0)
        head = dummy
        while len(heap) > 0:
            val, node = heappop(heap)
            head.next = node
            head = head.next
            if node.next != None:
                heappush(heap, (node.next.val, node.next))
        head.next = None
        return dummy.next  


