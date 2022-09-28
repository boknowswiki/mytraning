#!/usr/bin/python -t

# linked list
# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_len = self.get_len(head)
        if n_len == 1 and n == 1:
            return None
        
        #print(n_len)
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        
        n = n_len - n
        
        for _ in range(n):
            prev = prev.next
            #print(prev.val)
        
        next = prev.next
        prev.next = prev.next.next
        next.next = None
        
        return dummy.next
        
    def get_len(self, node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
            
        return cnt
